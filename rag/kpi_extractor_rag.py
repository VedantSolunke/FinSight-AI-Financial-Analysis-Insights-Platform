import os
from types import SimpleNamespace

from dotenv import load_dotenv
from pydantic import AliasChoices, BaseModel, ConfigDict, field_validator, Field

from llm.azure_openai import get_structured_completion
from vectorstore.azure_ai_search import AzureAISearchVectorStore

load_dotenv()


class FinancialMetrics(BaseModel):
    # The fallback (non-structured) path returns whatever key spelling the model
    # chooses, so accept the spaced, camel-case and snake-case variants.
    model_config = ConfigDict(populate_by_name=True)

    revenue: str | int | None = Field(None, validation_alias=AliasChoices("Revenue", "revenue"))
    net_income: str | int | None = Field(None, validation_alias=AliasChoices("Net Income", "NetIncome", "net_income"))
    operating_income: str | int | None = Field(None, validation_alias=AliasChoices("Operating Income", "OperatingIncome", "operating_income"))
    cash_flow: str | int | None = Field(None, validation_alias=AliasChoices("Cash Flow from Operating Activities", "CashFlowFromOperatingActivities", "cash_flow"))
    total_assets: str | int | None = Field(None, validation_alias=AliasChoices("Total Assets", "TotalAssets", "total_assets"))
    total_liabilities: str | int | None = Field(None, validation_alias=AliasChoices("Total Liabilities", "TotalLiabilities", "total_liabilities"))
    risk_factors: str | list | None = Field(None, validation_alias=AliasChoices("Top Risk Factors", "TopRiskFactors", "risk_factors"))
    growth_drivers: str | list | None = Field(None, validation_alias=AliasChoices("Top Growth Drivers", "TopGrowthDrivers", "growth_drivers"))


class Retriever:
    def __init__(self, client):
        self.client = client

    def invoke(
        self,
        query: str,
        company: str | None = None,
        year: int | None = None,
        top_k: int = 20
    ) -> list:
        """
        Retrieve relevant chunks from Azure AI Search.
        """
        filter_expr = None

        if company and year:
            filter_expr = (
                f"company eq '{company}' "
                f"and year eq '{year}'"
            )

        results = (
            self.client.search(
                search_text=query,
                top=top_k,
                filter=filter_expr
            )
            if filter_expr
            else self.client.search(
                search_text=query,
                top=top_k
            )
        )

        documents = []

        for result in results:
            content = result.get("content", "")
            documents.append(
                SimpleNamespace(
                    page_content=content
                )
            )

        return documents


CONTEXT_QUERIES = [
    "consolidated balance sheets total assets total liabilities stockholders equity",
    "consolidated statements of income revenues net income operating income",
    "consolidated statements of cash flows net cash provided by operating activities",
    "risk factors could adversely affect our business",
    "growth drivers revenue increase primarily driven by",
]


def retrieve_context(
    retriever: Retriever,
    company: str,
    year: int
) -> str:
    """
    Retrieve financial context with one targeted query per topic so that
    statements like the balance sheet are not crowded out by other sections.
    """
    seen = set()
    sections = []

    for query in CONTEXT_QUERIES:
        documents = retriever.invoke(
            query=f"{company} {year} {query}",
            company=company,
            year=year,
            top_k=6
        )
        for doc in documents:
            if doc.page_content not in seen:
                seen.add(doc.page_content)
                sections.append(doc.page_content)

    return "\n\n".join(sections)


def build_extraction_prompt(
    company: str,
    year: int,
    context: str
) -> str:
    """
    Build KPI extraction prompt.
    """
    return f"""
You are an expert financial analyst.

Company: {company}
Year: {year}

Context:
{context}

Extract the following information:

1. Revenue
2. Net Income
3. Operating Income
4. Cash Flow from Operating Activities
5. Total Assets
6. Total Liabilities
7. Top Risk Factors
8. Top Growth Drivers

Instructions:

- Use only the provided context.
- Return null if unavailable.
- Financial values must match the report exactly.
- Risk factors should be concise.
- Growth drivers should be concise.
- Return valid JSON only.
"""


def extract_financial_metrics(
    retriever: Retriever,
    company: str,
    year: int
) -> dict:
    """
    Extract KPIs using RAG.
    """
    context = retrieve_context(
        retriever=retriever,
        company=company,
        year=year
    )

    prompt = build_extraction_prompt(
        company=company,
        year=year,
        context=context
    )

    metrics = get_structured_completion(
        prompt=prompt,
        response_model=FinancialMetrics
    )

    return metrics.model_dump()


def main() -> None:
    company = "Apple"
    year = 2024

    vector_store = AzureAISearchVectorStore(
        endpoint=os.getenv("AZURE_SEARCH_ENDPOINT"),
        api_key=os.getenv("AZURE_SEARCH_API_KEY"),
        index_name=os.getenv("AZURE_SEARCH_INDEX_NAME")
    )

    retriever = Retriever(
        vector_store.client
    )

    results = extract_financial_metrics(
        retriever=retriever,
        company=company,
        year=year
    )

    print(f"\nExtracted KPIs for {company} {year}\n")

    for key, value in results.items():
        print(f"{key}:")
        print(value)
        print("-" * 80)


    from database.save_metrics import save_metrics

    save_metrics(
        company=company,
        year=year,
        metrics=results
    )

if __name__ == "__main__":
    main()