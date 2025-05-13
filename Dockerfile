# ---------- STAGE 1: BUILD ENVIRONMENT ----------
FROM python:3.13 as builder

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

# Pré-instale build deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    libgl1-mesa-glx \
    libxml2-dev \
    libxslt1-dev \
    && rm -rf /var/lib/apt/lists/*

# Copie apenas requirements
COPY requirements.txt .

# Use índice customizado para torch
RUN pip install --upgrade pip && \
    pip install --no-cache-dir --extra-index-url https://download.pytorch.org/whl/cpu -r requirements.txt

# ---------- STAGE 2: RUNTIME ENVIRONMENT ----------
FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /curriculum-vitae-query-assistant

# Copie dependências instaladas da imagem anterior
COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copie apenas o projeto (depois das dependências para manter cache)
COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
