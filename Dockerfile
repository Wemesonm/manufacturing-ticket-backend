FROM python:3.12-slim

# -----------------------------
# 1. Configurações básicas
# -----------------------------
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# -----------------------------
# 2. Dependências de sistema
# -----------------------------
# - build-essential / libpq-dev: necessários para psycopg2 (Postgres)
# - postgresql-client: para usar pg_isready no entrypoint
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    postgresql-client \
 && rm -rf /var/lib/apt/lists/*

# -----------------------------
# 3. Diretório de trabalho
# -----------------------------
WORKDIR /backend

# -----------------------------
# 4. Instala dependências Python
# -----------------------------
# Copia apenas requirements primeiro para aproveitar cache de build
COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# -----------------------------
# 5. Copia o restante do projeto
# -----------------------------
COPY . .

# -----------------------------
# 6. Script de entrada
# -----------------------------
# Certifique-se de que entrypoint.sh está na raiz do projeto
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 8000

# -----------------------------
# 7. EntryPoint
# -----------------------------
ENTRYPOINT ["/entrypoint.sh"]