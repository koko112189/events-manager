#!/bin/bash

# Esperar a que la base de datos esté lista
echo "Esperando a que la base de datos esté lista..."
while ! nc -z db 5432; do
  sleep 1
done
echo "La base de datos está lista."

# Ejecutar migraciones
echo "Ejecutando migraciones de Alembic..."
alembic upgrade head

# Iniciar la aplicación
echo "Iniciando la aplicación..."
exec "$@"
