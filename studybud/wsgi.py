"""
WSGI config for studybud project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""
from whitenoise import WhiteNoise

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studybud.settings')

application = get_wsgi_application()

application = WhiteNoise(application, root='/opt/render/project/src/staticfiles')