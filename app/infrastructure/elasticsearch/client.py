from elasticsearch import AsyncElasticsearch
from app.config.settings import settings

elasticsearch_client = AsyncElasticsearch(settings.ELASTICSEARCH_URL)