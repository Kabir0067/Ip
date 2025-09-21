import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")

from vercel_wsgi import handle
from server.wsgi import application 


def handler(request, response):
    return handle(request, response, application)
