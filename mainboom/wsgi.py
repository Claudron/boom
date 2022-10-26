"""
WSGI config for mainboom project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

if "RENDER" in os.environ:
    os.environ["DJANGO_SETTINGS_MODULE"] = "mainboom.settings.production"
else:
    os.environ["DJANGO_SETTINGS_MODULE"] = "mainboom.settings.dev"


application = get_wsgi_application()
