# Dockerfile
FROM python:3.13-slim
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir uv
RUN uv sync --frozen