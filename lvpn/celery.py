# coding=utf-8
import os, sys

from celery import Celery
# from django.utils import timezone
from django.apps import apps
from kombu import Queue

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lvpn.settings')

app = Celery('lvpn')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: [n.name for n in apps.get_app_configs()])
# app.now = timezone.now
app.conf.task_default_queue = 'default'
app.conf.task_queues = (
    Queue('default', routing_key='default'),
)

app.conf.task_routes = {
    'apps.users.tasks.send_token': {
        'queue': 'default',
        'routing_key': 'default',
    },
}
