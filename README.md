Events Manager

Events Manager es una aplicación para gestionar eventos, sesiones, ponentes y asistentes. Está construida con FastAPI, PostgreSQL, Elasticsearch, Redis y Celery para tareas asíncronas.

Requisitos

Docker

Docker Compose

Configuración

1. Clonar el repositorio

git clone https://github.com/tu-usuario/events-manager.git
cd events-manager

2. Configurar variables de entorno

Crea un archivo .env en la raíz del proyecto con las siguientes variables:

DATABASE_URL=postgresql+psycopg2://user:password@db:5432/events_manager
ELASTICSEARCH_URL=http://elasticsearch:9200
REDIS_URL=redis://redis:6379/0
SENDGRID_API_KEY=your_sendgrid_api_key
EMAIL_FROM=no-reply@miseventos.com
SMTP_SERVER=sandbox.smtp.mailtrap.io
SMTP_PORT=2525
SMTP_USERNAME=8d4efa6b068337
SMTP_PASSWORD=e9a723fd05dcef

3. Iniciar los servicios

Ejecuta el siguiente comando para construir y levantar los contenedores:

docker-compose up --build

Esto iniciará los siguientes servicios:

web: La aplicación FastAPI en http://localhost:8000.

db: Base de datos PostgreSQL.

elasticsearch: Motor de búsqueda Elasticsearch.

redis: Servidor Redis para manejar colas de tareas.

celery_worker: Worker de Celery para procesar tareas asíncronas.

celery_beat: Scheduler de Celery para tareas periódicas.

Servicios

1. FastAPI (Web)

La aplicación principal está disponible en http://localhost:8000. Puedes acceder a la documentación interactiva de la API en:

Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

2. PostgreSQL (DB)

La base de datos PostgreSQL está disponible en el puerto 5433. Puedes conectarte usando las siguientes credenciales:

Usuario: user

Contraseña: password

Base de datos: events_manager

3. Elasticsearch

Elasticsearch está disponible en http://localhost:9200. Se utiliza para la búsqueda e indexación de eventos y sesiones.

4. Redis

Redis está disponible en redis://localhost:6379. Se utiliza como broker para Celery.

5. Celery Worker

El worker de Celery procesa tareas asíncronas, como el envío de correos electrónicos.

6. Celery Beat

Celery Beat se encarga de ejecutar tareas periódicas, como notificaciones programadas.

Uso

1. Acceder a la API

Una vez que los contenedores estén en ejecución, puedes acceder a la API en http://localhost:8000.

2. Ejecutar migraciones

Si necesitas ejecutar migraciones para la base de datos, puedes hacerlo dentro del contenedor web:

docker exec -it events-manager-web alembic upgrade head

3. Detener los servicios

Para detener los contenedores, ejecuta:

docker-compose down


Configuración de Correo Electrónico

El proyecto utiliza Mailtrap como servidor SMTP para pruebas. Puedes cambiar la configuración en el archivo .env para usar un servidor SMTP real, como Gmail o SendGrid.

Ejemplo con Gmail

SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=tu-email@gmail.com
SMTP_PASSWORD=tu-contraseña

Nota: Si usas Gmail, asegúrate de habilitar el acceso de aplicaciones menos seguras o generar una contraseña de aplicación.
