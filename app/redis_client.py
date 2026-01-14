from redis import Redis
from redis.exceptions import RedisError


from app.config import settings # достаем настройки redis из конфига


def get_redis_client() -> Redis:
    """Создаем redis клиента"""
    client = Redis.from_url(settings.redis_url, decode_responses=True)
    return client


def ping_redis() -> bool:
    """Тест redis"""
    try:
        client = get_redis_client()
        result = client.ping()
        return bool(result)
    except RedisError as e:
        return False

#
