from django.urls import path
# from . import views
from .views import map, upload

urlpatterns = [
    path('map', map.view),
    path('upload', upload.view),
]