from vercel_wsgi import handle
from server.wsgi import application

# Vercel expects a top-level handler(request, context)
# This adapts Django's WSGI application to Vercel's serverless function.
def handler(request, context):
    return handle(request, context, application)
