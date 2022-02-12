FROM python:3.9-slim
WORKDIR /app
ENV PYTHONPATH="/app:$PYTHONPATH"

RUN apt-get update && apt-get install -y \
    git \
    curl \
    wget \
    build-essential \
    libmecab-dev \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN pip install poetry

COPY pyproject.toml ./
COPY poetry.lock ./
RUN poetry install
