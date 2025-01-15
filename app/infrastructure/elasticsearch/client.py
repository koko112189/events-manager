from elasticsearch import AsyncElasticsearch
from app.config import settings

elasticsearch_client = AsyncElasticsearch(settings.ELASTICSEARCH_URL)