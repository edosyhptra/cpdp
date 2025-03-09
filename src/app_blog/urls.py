from django.urls import path
# from . import views
from .views import list, read

urlpatterns = [
    path('', list.view),
    path('id/<str:id>', read.view),
]