import os
from worker import config
from celery import  Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'swiper.settings')

celery_app = Celery('swiper')
celery_app.config_from_object(config)
celery_app.autodiscover_tasks()


def call_by_worker(func):
    task = celery_app.task(func)
    return task.__name__

