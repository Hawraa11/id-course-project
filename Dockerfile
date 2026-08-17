# Builder stage
FROM python:3.10-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --user -r requirements.txt && \
    pip install --no-cache-dir --user httpx pytest

# Runtime stage
FROM python:3.10-slim

WORKDIR /app

COPY --from=builder /root/.local /root/.local
COPY app ./app
COPY tests ./tests

RUN adduser --disabled-password --gecos '' app && \
    chown -R app:app /app

ENV PATH=/root/.local/bin:$PATH

USER app

EXPOSE 8001

CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]
