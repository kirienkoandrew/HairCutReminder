"""Celery worker

# команда для запуска celery: celery -A celery_worker.celery_app worker -l INFO
# redis должен быть запущен
"""

from app.tasks import celery_app

# Экспортируем celery_app для использования в командах celery
__all__ = ['celery_app']

