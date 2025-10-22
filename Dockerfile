# Base image
FROM python:3.12-slim

# Install system dependencies (optional, для некоторых пакетов)
RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

# Install uv
RUN pip install uv

# Set workdir
WORKDIR /app

# Copy project
COPY . .

# Install Python dependencies via uv
RUN uv sync --frozen

# Expose port for Django
EXPOSE 8000

# Default command
CMD ["uv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
