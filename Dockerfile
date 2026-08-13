# Builder stage
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --user -r requirements.txt

# Runtime stage
FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /root/.local /root/.local
COPY app ./app

RUN adduser --disabled-password --gecos '' app && \
    chown -R app:app /app

ENV PATH=/root/.local/bin:$PATH

USER app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
