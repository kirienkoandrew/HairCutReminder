from fastapi import APIRouter

from app.redis_client import ping_redis

router = APIRouter()


@router.get("/health")
async def health_check():
    # TODO доделать проверку бота и celery
    redis_ok = ping_redis()
    return {"API": "ok",
            "redis": redis_ok}
