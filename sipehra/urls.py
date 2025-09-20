# sipehra/urls.py
from django.urls import path
from .views import home_view, save_location, love_view
from django.views.decorators.http import require_http_methods

urlpatterns = [
    path("", home_view, name="home"),
    path("save-location/", require_http_methods(["POST"])(save_location), name="save_location"),
    path("love/", love_view, name="love"),
]
