FROM python:3.13-slim as builder

WORKDIR /app

COPY requirement.txt .

RUN pip install --no--cache-dir -r requirements.txt


FROM python:3.13-slim

WORKDIR /app

COPY --from=builder /app /app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

