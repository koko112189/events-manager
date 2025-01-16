
import redis
from app.config.settings import settings

redis_client = None

def get_redis():
    global redis_client
    if not redis_client:
        redis_client = redis.StrictRedis.from_url(f"{settings.REDIS_URL}", decode_responses=True, encoding="utf-8")
        
        # await aioredis.from_url(
        #     f"{settings.REDIS_URL}",
        #     encoding="utf-8",
        #     decode_responses=True
        # )
    return redis_client
