import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Portals.settings')

app = Celery('Portals')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send_every_monday_8am': {
        'task': 'NewsPortal.tasks.week_post',
        'schedule': crontab(day_of_week="monday", hour=8, minute=0),
    },
}