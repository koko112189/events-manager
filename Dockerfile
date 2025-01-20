# Dockerfile
FROM python:3.12-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && apt-get clean

# Instalar Poetry
RUN pip install --no-cache-dir poetry

RUN poetry config virtualenvs.create false

# Copiar los archivos de configuración
COPY pyproject.toml poetry.lock ./

COPY .env ./

# Instalar dependencias
RUN poetry install --no-interaction --no-ansi --no-root

# Copiar el código fuente
COPY . .

# Exponer el puerto de la aplicación
EXPOSE 8000

# Comando de inicio
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
