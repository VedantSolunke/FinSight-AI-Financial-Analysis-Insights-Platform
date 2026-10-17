
FROM python:3.12-slim

WORKDIR /app

# Give pip more time for slow downloads and retry failures
ENV PIP_DEFAULT_TIMEOUT=300
ENV PIP_RETRIES=10
ENV UV_HTTP_TIMEOUT=300
ENV UV_HTTP_RETRIES=10

# Install uv
RUN python -m pip install --no-cache-dir uv

# Install dependencies separately for better layer caching
COPY requirements.txt ./
RUN uv pip install --system --no-cache -r requirements.txt

# Copy application code
COPY . /app

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
