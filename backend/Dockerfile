# Dockerfile
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install TiMidiTy
RUN apt-get update && apt-get install -y timidity

# Install Poetry
RUN pip install poetry

# Create and set working directory
WORKDIR /app

# Copy project files
COPY pyproject.toml poetry.lock /app/

# Install dependencies
RUN poetry install --no-root --no-interaction --no-ansi

# Copy application files
COPY . /app/

# Command to run the application
CMD ["poetry", "run", "uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
