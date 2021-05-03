from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('dojo', views.create_dojo),
    path('ninja', views.create_ninja),
    path('delete', views.delete_dojo)
]