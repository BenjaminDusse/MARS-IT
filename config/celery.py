# import os
# from domains.models import Domain

# from celery import Celery

# # Set the default Django settings module for the 'celery' program.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# app = Celery('config')

# # Using a string here means the worker doesn't have to serialize
# # the configuration object to child processes.
# # - namespace='CELERY' means all celery-related configuration keys
# #   should have a `CELERY_` prefix.
# app.config_from_object('django.conf:settings', namespace='CELERY')

# # Load task modules from all registered Django apps.
# app.autodiscover_tasks()


# @app.task(bind=True) # func ga self argument ham keladi # 
# def debug_task(self, domain: Domain):
#     print(f'Request: {self.request!r}')

#     # logika ketadi.

# # har kuni ishlashi uchun kod kerak
# # alohida run qilish kerak celeryni celery workerlarni
# # celery -A config worker -l info

# # celery -A config beat -l info # beat yani har kuni ishlab turishi uchun komanda



# Real Python

import os
from celery.schedules import crontab
# import crontab

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("config")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'every-day-parser': {
        'task': 'main.tasks.parse_every_day_posts',
        'schedule': crontab(hour=23),
    },
}

