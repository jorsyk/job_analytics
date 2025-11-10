# ====== 1. Builder stage ======
FROM python:3.13-slim AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential libpq-dev && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# ====== 2. Final stage ======
FROM python:3.13-slim

WORKDIR /app

COPY --from=builder /usr/local /usr/local

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]