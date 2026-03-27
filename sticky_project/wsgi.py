"""WSGI config for sticky_project."""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sticky_project.settings')
application = get_wsgi_application()
