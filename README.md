# FinSight AI — Financial Analysis & Investor Intelligence Platform

<p align="center">
  <strong>AI-powered financial document intelligence using RAG, Azure OpenAI, Azure AI Search, FastAPI, PostgreSQL, Docker, AKS and GitHub Actions.</strong>
</p>

<p align="center">
  <a href="https://github.com/VedantSolunke/FinSight-AI-Financial-Analysis-Insights-Platform">
    <img src="https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github" alt="GitHub Repository">
  </a>
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.12">
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/Azure-Cloud-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white" alt="Microsoft Azure">
  <img src="https://img.shields.io/badge/Azure%20OpenAI-LLM-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white" alt="Azure OpenAI">
  <img src="https://img.shields.io/badge/RAG-AI%20Retrieval-7B61FF?style=for-the-badge" alt="RAG">
  <img src="https://img.shields.io/badge/PostgreSQL-Database-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/Docker-Container-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/AKS-Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white" alt="AKS">
</p>

> **FinSight AI** is an end-to-end financial document intelligence platform that turns annual reports into searchable, structured financial insights and grounded AI research. It combines document processing, semantic chunking, retrieval-augmented generation (RAG), KPI extraction, PostgreSQL persistence, an interactive dashboard, and an AI chatbot, then packages and deploys the application to Azure Kubernetes Service.

---

## Project Overview

FinSight AI is designed around a practical financial-analysis workflow:

1. An investor uploads a company annual report.
2. The PDF is converted into Markdown.
3. The document is divided into semantically meaningful chunks.
4. Chunks are embedded and indexed in Azure AI Search.
5. Relevant report content is retrieved for financial questions.
6. GPT-5 processes the retrieved context.
7. Financial KPIs are returned as structured data.
8. KPI results are persisted in PostgreSQL.
9. The dashboard presents reusable financial insights.
10. Users can ask follow-up questions through a RAG-powered chatbot.

The platform was developed incrementally from architecture → application implementation → Azure integration → containerization → AKS deployment → CI/CD automation.

---

## Problem Statement

Financial annual reports contain large amounts of unstructured information spread across financial statements, business descriptions, risk disclosures, growth commentary and other sections.

Traditional manual analysis creates several problems:

- Long reports take significant time to review.
- Relevant information is distributed across many pages.
- Repeated KPI extraction is inefficient.
- Searching for context across multiple reports is cumbersome.
- Dashboard values should not require an LLM call every time they are displayed.
- A conversational interface needs access to the underlying source material rather than relying only on model memory.

### Target Problem

> **How can financial reports be transformed into a searchable, structured and reusable knowledge layer that supports both KPI analytics and grounded natural-language financial research?**

---

## Solution

FinSight AI uses a two-path intelligence architecture:

### Structured Financial Intelligence

Annual reports are processed once, relevant financial information is extracted with RAG + GPT-5, and the resulting KPI data is stored in PostgreSQL.

```text
Annual Report
     │
     ▼
PDF → Markdown
     │
     ▼
Semantic Chunking
     │
     ▼
Embeddings
     │
     ▼
Azure AI Search
     │
     ▼
KPI Retrieval
     │
     ▼
GPT-5
     │
     ▼
Structured KPI Data
     │
     ▼
PostgreSQL
     │
     ▼
Dashboard
```

### Conversational Financial Research

Users can ask questions about indexed financial reports. Relevant content is retrieved before GPT-5 generates the response.

```text
User Question
     │
     ▼
Azure AI Search
     │
     ▼
Relevant Report Context
     │
     ▼
GPT-5
     │
     ▼
Natural-Language Answer
```

This separation allows frequently displayed dashboard information to be persisted while keeping conversational analysis dynamic.

---

## Objectives

### Product Objectives

- Simplify financial-report analysis.
- Convert unstructured annual reports into searchable knowledge.
- Extract reusable financial KPIs.
- Provide a dashboard for company-level financial insights.
- Enable natural-language financial research.
- Support comparison and filtering by company/year.
- Demonstrate an end-to-end cloud deployment model.

### Engineering Objectives

- Build a modular Python/FastAPI application.
- Apply RAG to document-based financial analysis.
- Integrate Azure AI services.
- Persist extracted results in PostgreSQL.
- Containerize the application with Docker.
- Deploy the application on Kubernetes/AKS.
- Automate deployment through GitHub Actions.
- Demonstrate practical cloud troubleshooting and deployment operations.

---

# Key Features

| Feature                    | Description                                              |
| -------------------------- | -------------------------------------------------------- |
| 📄 Financial Report Upload | Upload annual reports through the web interface          |
| 🔄 PDF → Markdown          | Converts source PDFs into LLM-friendly Markdown          |
| 🧩 Semantic Chunking       | Creates semantically meaningful document chunks          |
| 🔎 Search Indexing         | Stores document chunks and metadata in Azure AI Search   |
| 🧠 RAG Retrieval           | Retrieves relevant source content before LLM generation  |
| 📊 KPI Extraction          | Extracts reusable financial metrics into structured data |
| 💾 Persistent KPI Storage  | Stores extracted results in PostgreSQL                   |
| 📈 Financial Dashboard     | Displays company KPIs, growth metrics and risk factors   |
| 🤖 AI Financial Chatbot    | Answers questions using indexed report context           |
| 🏢 Company Filtering       | Supports company/year-oriented analysis                  |
| ☁️ Azure Deployment        | Runs the application on Azure Kubernetes Service         |
| 🐳 Containerization        | Packages the application as a Docker image               |

---

<!-- # Implemented Scope vs Future Enhancements

A major goal of this README is to distinguish what was actually demonstrated from what was discussed as a production improvement.

| Area                        |     Implemented     | Future / Proposed                           |
| --------------------------- | :-----------------: | ------------------------------------------- |
| Financial PDF ingestion     |         ✅          | —                                           |
| PDF → Markdown              |         ✅          | —                                           |
| Semantic chunking           |         ✅          | —                                           |
| Azure OpenAI embeddings     |         ✅          | —                                           |
| Azure AI Search             |         ✅          | Hybrid retrieval improvements               |
| BM25 retrieval              |         ✅          | Semantic / hybrid retrieval                 |
| GPT-5 KPI extraction        |         ✅          | More advanced agent workflows               |
| PostgreSQL persistence      |         ✅          | Data lifecycle / richer modeling            |
| Dashboard                   |         ✅          | More analytics                              |
| RAG chatbot                 |         ✅          | Guardrails + richer agent orchestration     |
| FastAPI backend             |         ✅          | Service decomposition if needed             |
| HTML/CSS UI                 |         ✅          | Separate frontend service if required       |
| Docker                      |         ✅          | Image optimization                          |
| Azure Container Registry    |         ✅          | Managed identity hardening                  |
| AKS deployment              |         ✅          | Autoscaling / multi-region                  |
| Application authentication  |         ❌          | Microsoft Entra ID / SSO                    |
| RBAC                        |         ❌          | Role-based authorization                    |
| MFA                         |         ❌          | Enterprise identity controls                |
| Azure Key Vault             |         ❌          | Centralized secret management               |
| Managed Identity            | Partially discussed | Passwordless Azure-to-Azure access          |
| Private networking          |         ❌          | VNet/private endpoints/VPN                  |
| Observability               |       Limited       | Centralized logs, metrics, APM              |
| Disaster recovery           |         ❌          | Automated backup/recovery                   |
| Multi-region                |         ❌          | Regional failover                           |
| AI governance               |         ❌          | Domain guardrails + responsible AI controls |

--- -->

# Architecture

## Architecture Philosophy

The project separates two architectural views:

- **Logical architecture** — how information moves through the application.

- **Physical architecture** — which cloud/platform services host each responsibility.

The architecture was designed before implementation and then implemented incrementally.

---

## Logical Architecture

![Logical FinSight-AI architecture diagram](diagrams/Logical_FinSight-AI%20Architecture%20Diagram.png)

---

## Physical Architecture

## ![Physical FinSight-AI architecture diagram ](diagrams/physical_FinSight-AI%20Azure%20Cloud%20Architecture.png)

# AI / RAG Pipeline

The project uses Retrieval-Augmented Generation rather than sending an entire annual report directly to the model for every question.

### 1. Document Preparation

Annual reports from companies such as Tesla, Apple and Microsoft are used as source documents.

### 2. PDF Conversion

`PyMuPDF4LLM` converts PDFs into Markdown suitable for downstream processing.

### 3. Semantic Chunking

LangChain's semantic chunking approach divides the Markdown into meaningful sections rather than relying only on fixed character boundaries.

### 4. Embeddings

Azure OpenAI embeddings convert document chunks into vector representations.

### 5. Search Indexing

Azure AI Search stores the searchable content and associated metadata.

The demonstrated index contains fields such as:

| Field            | Purpose                        |
| ---------------- | ------------------------------ |
| `id`             | Chunk/document identifier      |
| `company`        | Company filtering              |
| `year`           | Fiscal/report year filtering   |
| `source_file`    | Source-document identification |
| `content`        | Searchable report text         |
| `content_vector` | Vector representation          |

### 6. Retrieval

The demonstrated retrieval strategy uses **BM25 keyword search**.

The project also discusses alternative retrieval approaches:

```text
Keyword Search
      +
Semantic Search
      ↓
Hybrid Search
```

but the implemented demonstration uses BM25.

### 7. LLM Processing

Retrieved context is passed to GPT-5 with a financial-analysis extraction prompt.

### 8. Structured Output

The KPI extraction path requests structured JSON so the result can be persisted and consumed by the dashboard.

Example shape:

```json
{
  "revenue": "...",
  "net_income": "...",
  "operating_income": "...",
  "operating_cash_flow": "...",
  "total_assets": "...",
  "total_liabilities": "...",
  "risk_factors": "...",
  "growth_drivers": "..."
}
```

---

# KPI Pipeline vs Chatbot Pipeline

These are intentionally treated as two related but different workloads.

## KPI Pipeline

```text
Document
  ↓
Chunk
  ↓
Search Index
  ↓
KPI Query
  ↓
Relevant Context
  ↓
GPT-5
  ↓
Structured JSON
  ↓
PostgreSQL
  ↓
Dashboard
```

**Why persist the result?**

Dashboard KPIs are repeatedly viewed. Persisting extracted results avoids regenerating the same KPI information for every dashboard request.

## Chatbot Pipeline

```text
User Question
  ↓
Search
  ↓
Relevant Context
  ↓
GPT-5
  ↓
Natural Language
  ↓
Chat Interface
```

The chatbot remains dynamic because each question can require a different retrieval context.

---

# Technology Stack

## Core Stack

| Layer              | Technology                                    |
| ------------------ | --------------------------------------------- |
| Language           | Python 3.12                                   |
| Backend            | FastAPI                                       |
| Frontend           | HTML / CSS / templates                        |
| Package Management | UV                                            |
| PDF Processing     | PyMuPDF4LLM                                   |
| Chunking           | LangChain Semantic Chunker                    |
| Embeddings         | Azure OpenAI Embeddings                       |
| LLM                | GPT-5 via Azure OpenAI / Microsoft Foundry    |
| Search / Retrieval | Azure AI Search                               |
| Retrieval Strategy | BM25                                          |
| Database           | Azure Database for PostgreSQL Flexible Server |
| DB Tooling         | pgAdmin                                       |
| API Testing        | FastAPI Swagger / OpenAPI                     |
| Containerization   | Docker                                        |
| Registry           | Azure Container Registry                      |
| Orchestration      | Azure Kubernetes Service                      |

## Cloud Platform

```text
Microsoft Azure
├── Azure OpenAI / Microsoft Foundry
├── Azure AI Search
├── Azure PostgreSQL
├── Azure Container Registry
└── Azure Kubernetes Service
```

---

# Architecture & Design Decisions

## 1. FastAPI for the Backend

**Decision:** Use FastAPI as the application/API layer.

**Why:**

- Python-native ecosystem fits the RAG and document-processing workloads.
- Async-capable API framework.
- Automatic OpenAPI/Swagger documentation.
- Simple route-based integration.
- Works naturally with the project's modular Python components.

**Trade-off:** The current implementation keeps UI and backend together instead of creating separate frontend/backend services.

---

## 2. HTML/CSS Instead of a Separate Frontend Service

**Decision:** Keep the UI integrated with the FastAPI application.

**Why:**

- Reduces project complexity.
- Reduces deployment overhead.
- Keeps the demonstration architecture compact.
- Avoids introducing another runtime/service for a project focused primarily on AI/RAG architecture.

**Trade-off:** Independent frontend/backend deployments would provide more flexibility at larger scale.

---

## 3. Azure AI Search

**Decision:** Use Azure AI Search as the retrieval/search layer.

**Why:**

- Fits naturally into the Azure-based architecture.
- Provides searchable document indexing.
- Supports metadata filtering.
- Provides a path toward vector and hybrid search.
- Reduces the need to operate a separate search infrastructure layer.

---

## 4. BM25 for Demonstrated Retrieval

**Decision:** Use BM25 keyword retrieval for the demonstrated query stage.

**Why:**

- Straightforward relevance mechanism.
- Works well with explicit financial terminology and report language.
- Avoids an additional query-embedding operation in the demonstrated workflow.
- Keeps retrieval easy to inspect and troubleshoot.

**Trade-off:** Semantic or hybrid retrieval can better capture conceptually similar language that does not share exact keywords.

---

## 5. Semantic Chunking

**Decision:** Use semantic chunking rather than only fixed-size chunks.

**Why:**

Financial reports contain sections with strong semantic boundaries. Keeping related content together provides more meaningful retrieval context.

---

## 6. PostgreSQL for Structured KPI Persistence

**Decision:** Store extracted KPI results in PostgreSQL.

**Why:**

- KPI data is structured.
- Dashboard reads are frequent and predictable.
- Persisted metrics can be queried without invoking the LLM again.
- Separates analytical persistence from document retrieval.

---

## 7. Docker

**Decision:** Containerize the application.

**Why:**

- Packages application code and runtime dependencies together.
- Reduces environment differences between local and cloud execution.
- Creates a deployable artifact that can be stored in ACR and executed by AKS.

---

## 8. AKS for Deployment

**Decision:** Use Azure Kubernetes Service.

**Why:**

- Provides managed Kubernetes infrastructure.
- Supports container orchestration.
- Provides a foundation for replicas, services and scaling.
- Integrates naturally with ACR and Azure networking.

**Trade-off:** AKS introduces more operational complexity than simpler managed application-hosting options.

For this project, AKS is valuable because Kubernetes deployment and cloud-native orchestration are part of the engineering objective.

---

# Strategies & Methodologies

## Architecture-First Development

The project follows:

```text
Business Requirements
        ↓
Logical Architecture
        ↓
Physical Architecture
        ↓
Implementation
        ↓
Cloud Integration
        ↓
Deployment
```

This avoids choosing technologies before understanding the business and system requirements.

---

## Incremental Implementation

The application was built and validated in stages:

1. PDF processing.
2. Chunking.
3. Embeddings.
4. Search index.
5. Retrieval.
6. LLM extraction.
7. Database.
8. APIs.
9. UI.
10. End-to-end testing.
11. Docker.
12. ACR.
13. AKS.

This approach makes failures easier to isolate.

---

## Validate Each Layer Independently

The project validates individual layers before relying on the full pipeline:

```text
PDF Conversion
      ↓
Chunking
      ↓
Search Index
      ↓
Retrieval
      ↓
LLM
      ↓
Database
      ↓
API
      ↓
UI
      ↓
Container
      ↓
AKS
```

This proved useful during troubleshooting because several failures occurred at different layers.

---

## Persist Reusable AI Results

Instead of recalculating dashboard KPIs repeatedly:

```text
Upload
  ↓
RAG + GPT-5
  ↓
PostgreSQL
  ↓
Repeated Dashboard Reads
```

This separates expensive AI processing from frequent dashboard reads.

---

# Project Structure

The documented implementation follows a modular layout similar to:

```text
FinSight-AI-Financial-Analysis-Insights-Platform/
│
├── data/
│   ├── raw/
│   └── markdown/
│
├── ingestion/
│   ├── __init__.py
│   ├── pdf_to_markdown.py
│   └── ingest_documents.py
│
├── chunking/
│   └── semantic_chunker.py
│
├── vector_store/
│   ├── azure_ai_search.py
│   └── create_index.py
│
├── rag/
│   ├── __init__.py
│   └── kpi_extractor_rag.py
│
├── llm/
│   └── azure_openai.py
│
├── database/
│   ├── postgresql.py
│   ├── create_table.py
│   └── save_metrics.py
│
├── routes/
│   ├── ingestion.py
│   ├── dashboard.py
│   └── chatbot.py
│
├── static/
│
├── templates/
│
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
│
├── .github/
│   └── workflows/
│       └── deploy.yaml
│
├── app.py
├── main.py
├── requirements.txt
├── Dockerfile
└── .env
```

> **Repository note:** The reports describe the implementation structure across the development series. If the current repository uses slightly different filenames, treat the repository tree as authoritative.

---

# Repository / Component Responsibilities

| Component            | Responsibility                                         |
| -------------------- | ------------------------------------------------------ |
| `ingestion/`         | PDF conversion and document ingestion                  |
| `chunking/`          | Semantic document chunking                             |
| `vector_store/`      | Azure AI Search index creation and document indexing   |
| `rag/`               | Retrieval + KPI extraction workflow                    |
| `llm/`               | Azure OpenAI configuration/client logic                |
| `database/`          | PostgreSQL connectivity, schema and KPI persistence    |
| `routes/`            | FastAPI endpoints for ingestion, dashboard and chatbot |
| `templates/`         | Server-rendered HTML UI                                |
| `static/`            | CSS/static frontend assets                             |
| `k8s/`               | Kubernetes deployment and service manifests            |
| `.github/workflows/` | GitHub Actions CI/CD                                   |
| `Dockerfile`         | Container image definition                             |
| `requirements.txt`   | Python dependencies                                    |
| `.env`               | Local environment configuration                        |

---

# Local Setup

## Prerequisites

Install:

- Python 3.12
- Git
- UV
- Azure CLI
- Docker Desktop — required for container deployment/testing
- `kubectl` — required for AKS deployment
- An Azure subscription for the cloud-backed RAG workflow

---

## 1. Clone the Repository

```bash
git clone https://github.com/VedantSolunke/FinSight-AI-Financial-Analysis-Insights-Platform.git

cd FinSight-AI-Financial-Analysis-Insights-Platform
```

---

## 2. Create the Python Environment

```bash
pip install uv
uv venv
```

Activate the environment.

### Windows

```powershell
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
uv pip install -r requirements.txt
```

---

# Environment Configuration

Create a `.env` file in the project root.

The application requires configuration for the Azure services used by the RAG pipeline.

Example structure:

```env
# Azure OpenAI
AZURE_OPENAI_ENDPOINT=<your-endpoint>
AZURE_OPENAI_API_KEY=<your-api-key>
AZURE_OPENAI_API_VERSION=<your-api-version>
AZURE_OPENAI_CHAT_DEPLOYMENT=<your-gpt-deployment>
AZURE_OPENAI_EMBEDDING_DEPLOYMENT=<your-embedding-deployment>

# Azure AI Search
AZURE_SEARCH_ENDPOINT=<your-search-endpoint>
AZURE_SEARCH_API_KEY=<your-search-api-key>
AZURE_SEARCH_INDEX=<your-index-name>

# PostgreSQL
POSTGRES_HOST=<your-postgres-host>
POSTGRES_PORT=5432
POSTGRES_DB=<your-database>
POSTGRES_USER=<your-username>
POSTGRES_PASSWORD=<your-password>
```

### Important

- Do **not** commit `.env`.
- Use your own Azure resources and credentials.
- Never place API keys/passwords directly in source code.
- For production deployments, use a centralized secret-management solution such as Azure Key Vault and managed identity where supported.

---

# Run the Application

## 1. Prepare the Search Index

Create the Azure AI Search index using the project's index-creation module.

The documented implementation uses an index named:

```text
financial_document
```

The index contains document content and metadata used during retrieval.

---

## 2. Process Documents

Place source annual reports in the appropriate raw-data directory.

The documented workflow converts PDFs to Markdown and then indexes the resulting chunks.

Example module execution:

```bash
python -m ingestion.ingest_documents
```

If the repository currently uses a different module/package name, use the corresponding entry point in the repository.

---

## 3. Start FastAPI

The documented application is served on port `8000`.

A typical local command is:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

Open:

```text
http://localhost:8000
```

---

# API Documentation

FastAPI provides interactive API documentation at:

```text
http://localhost:8000/docs
```

The documented API surface includes functionality for:

- Health checks
- Document ingestion
- Dashboard data
- Chatbot/RAG interaction

Swagger/OpenAPI can be used to test the APIs independently of the web UI.

---

# Docker

## Build the Image

The deployment guide uses:

```bash
docker build -t invint .
```

## Run Locally

```bash
docker run -p 8000:8000 invint
```

Open:

```text
http://localhost:8000
```

### Container Validation Checklist

Verify:

- Application loads.
- Dashboard renders.
- PDF upload works.
- Search/RAG workflow works.
- Chatbot responds.
- Database-backed KPI information is available.

---

# Azure Deployment

The documented deployment path is:

```text
Local Docker Image
       ↓
Azure Container Registry
       ↓
Azure Kubernetes Service
       ↓
Kubernetes Deployment
       ↓
Pod
       ↓
LoadBalancer
       ↓
Public Application
```

## 1. Azure Login

```bash
az login
az account show
```

---

## 2. Login to ACR

Example:

```bash
az acr login --name invintelligence
```

---

## 3. Tag the Image

```bash
docker tag invint:latest invintelligence.azurecr.io/invint:v1
```

---

## 4. Push to ACR

```bash
docker push invintelligence.azurecr.io/invint:v1
```

Verify:

```bash
az acr repository list --name invintelligence --output table
```

---

## 5. Connect to AKS

```bash
az aks get-credentials \
  --resource-group rg-inv-intelligence \
  --name inv-intelligence-aks \
  --overwrite-existing
```

Verify:

```bash
kubectl get nodes
```

---

## 6. Attach ACR to AKS

```bash
az aks update \
  --resource-group rg-inv-intelligence \
  --name inv-intelligence-aks \
  --attach-acr invintelligence
```

Check:

```bash
az aks check-acr \
  --resource-group rg-inv-intelligence \
  --name inv-intelligence-aks \
  --acr invintelligence
```

---

## 7. Deploy Kubernetes Resources

If the repository contains Kubernetes manifests:

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

Verify:

```bash
kubectl get deployments
kubectl get pods
kubectl get svc
```

---

## 8. Expose the Application

The demonstrated service configuration maps external port `80` to application port `8000`.

```bash
kubectl expose deployment invint \
  --type=LoadBalancer \
  --port=80 \
  --target-port=8000
```

Get the public endpoint:

```bash
kubectl get svc
```

Then access:

```text
http://<external-ip>
```

---

# Validation & Testing

The project was validated incrementally and through complete end-to-end workflows.

## Document Processing Validation

Example validation performed with annual reports included:

- Apple
- Tesla
- Microsoft

The Tesla end-to-end test demonstrated the complete flow:

```text
Tesla PDF
   ↓
PDF → Markdown
   ↓
Semantic Chunking
   ↓
Embeddings
   ↓
Azure AI Search
   ↓
KPI Retrieval
   ↓
GPT-5
   ↓
Structured KPI Output
   ↓
PostgreSQL
   ↓
Dashboard
```

## Retrieval Validation

The retrieval layer was checked independently before enabling the complete GPT extraction flow.

## API Validation

FastAPI Swagger `/docs` was used to test API behavior.

## Deployment Validation

The AKS deployment was checked through:

```bash
kubectl get nodes
kubectl get deployments
kubectl get pods
kubectl get svc
kubectl logs <pod-name>
```

---

# Cost Considerations

The architecture was intentionally kept relatively compact to reduce unnecessary cloud services.

### Cost-producing components discussed

- Azure OpenAI / GPT usage.
- Embedding generation.
- Azure AI Search.
- Azure PostgreSQL.
- AKS compute.
- Azure Container Registry.
- Other supporting Azure resources.

### Cost-aware design decisions

1. Persist KPI results in PostgreSQL rather than regenerating them for every dashboard request.
2. Keep UI and backend together for the current project.
3. Avoid unnecessary caching infrastructure.
4. Use small/test-oriented AKS configurations during demonstration.
5. Clean up Azure resources after testing where appropriate.

> Azure pricing changes over time and depends on region, tier, usage and subscription. Do not treat demonstration costs as current fixed pricing.

---

# Screenshots & Visuals

The repository can be made even more presentation-ready by storing UI screenshots under a directory such as:

```text
docs/
└── images/
    ├── dashboard.png
    ├── chatbot.png
    ├── report-upload.png
    ├── company-analysis.png
    └── aks-deployment.png
```

Recommended README placement:

### Dashboard

```markdown
![FinSight AI Dashboard](docs/images/dashboard.png)
```

### AI Research / Chatbot

```markdown
![FinSight AI Chatbot](docs/images/chatbot.png)
```

### Architecture

The Mermaid diagrams in this README are intentionally used as repository-native visuals so the architecture remains readable without requiring external diagram files.

---

# What This Project Demonstrates

From a technical-review perspective, the project demonstrates experience across several layers of modern AI application engineering.

### AI / GenAI

- Retrieval-Augmented Generation.
- Financial document intelligence.
- Prompt-based structured extraction.
- GPT-5 integration.
- Embeddings.
- Search/retrieval design.
- AI cost considerations.

### Backend Engineering

- Python.
- FastAPI.
- Modular application structure.
- API design.
- Swagger/OpenAPI.
- Database persistence.

### Data / Search

- PDF processing.
- Markdown transformation.
- Semantic chunking.
- Metadata design.
- BM25 retrieval.
- Azure AI Search.
- Structured KPI persistence.

### Cloud Engineering

- Azure resource provisioning.
- Azure OpenAI.
- Azure AI Search.
- Azure PostgreSQL.
- Azure Container Registry.
- Azure Kubernetes Service.

### DevOps

- Docker.
- Kubernetes.
- Kubernetes manifests.
- GitHub Actions.
- Service-principal authentication.
- Secrets management.
- Automated deployment.
- Deployment troubleshooting.

### Architecture

- Business requirements → architecture → implementation.
- Logical vs physical architecture.
- Component responsibility separation.
- Cost-aware architecture.
- Production-readiness analysis.
- Security and scalability roadmap.

---

# Important Architectural Notes

### Current Application Boundary

The current application combines UI and backend responsibilities in a single deployable service.

```text
Single Application
├── FastAPI
├── HTML/CSS UI
├── RAG workflow
├── Dashboard
└── Chatbot
```

The project documentation identifies independent frontend/backend services as a possible enterprise evolution.

### Current Retrieval Boundary

The demonstrated retrieval implementation uses BM25 keyword search.

Semantic/vector and hybrid retrieval are discussed as possible improvements.

### Current Security Boundary

The deployed demonstration is publicly accessible and does not implement full application authentication/RBAC.

The final project review explicitly treats identity, network security and secret-management hardening as future work.

---

# Disclaimer

This repository documents a portfolio/learning implementation of an AI-powered financial intelligence platform.

The system is designed to demonstrate:

- Financial document processing.
- RAG architecture.
- AI-assisted KPI extraction.
- Cloud integration.
- Containerization.
- Kubernetes deployment.
- CI/CD.

It should **not** be interpreted as a regulated investment-advisory system or as a substitute for professional financial analysis, accounting review or investment advice.

AI-generated financial insights should be validated against the underlying source documents.

---

## Built With

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,fastapi,docker,kubernetes,github,githubactions,postgres,azure" alt="Technology icons">
</p>

<p align="center">
  <strong>FinSight AI</strong><br>
  Financial documents → RAG → Structured insights → Dashboard → AI research → Azure deployment
</p>
