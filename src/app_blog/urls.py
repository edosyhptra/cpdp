from django.urls import path
# from . import views
from .views import list, read, create

urlpatterns = [
    path('', list.view),
    path('id/<str:id>', read.view),
    path('create/', create.view),
]