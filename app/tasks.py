from celery import Celery

from app.config import settings


celery_app = Celery(
    settings.project_name,
    broker=settings.redis_url,
    backend=settings.redis_url,
)


celery_app.conf.update(
    timezone='UTC',
    enable_utc=True,
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    broker_connect_retry_on_startup=True,
    result_expires=3600,
    task_default_queue='newsbot',
)


@celery_app.task(name='app.tasks.ping')
def ping() -> str:
    return "pong"