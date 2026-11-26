import redis.asyncio as redis
from pydantic_settings import BaseSettings

class RedisSettings(BaseSettings):
    REDIS_HOST: str
    REDIS_PORT: int

    class Config:
        env_file = ".env.docker"

redis_settings = RedisSettings()

# Создаем пул соединений
redis_pool = redis.ConnectionPool(
    host=redis_settings.REDIS_HOST, 
    port=redis_settings.REDIS_PORT, 
    db=0, 
    decode_responses=True
)

async def get_redis():
    return redis.Redis(connection_pool=redis_pool)