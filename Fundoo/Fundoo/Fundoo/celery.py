import os
from celery import Celery
from django.conf import settings
from .settings import BROKER_URL

# Setting the default django settings in the tasks.py program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Fundoo.settings')
app = Celery('Fundoo', broker=BROKER_URL)


app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


