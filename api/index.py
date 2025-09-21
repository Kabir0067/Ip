import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")

from vercel_wsgi import handle
from server.wsgi import application  # wsgi.py-и Django

def handler(request, response):
    return handle(request, response, application)
