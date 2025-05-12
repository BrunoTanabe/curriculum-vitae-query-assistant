FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    git \
    curl \
    && apt-get clean

COPY pyproject.toml .
COPY . .

RUN pip install --upgrade pip setuptools wheel \
    && pip install .

EXPOSE 8000

CMD ["gunicorn", "setup.wsgi:application", "--bind", "0.0.0.0:8000"]
