from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage)         # Inclui as urls do app blog
]