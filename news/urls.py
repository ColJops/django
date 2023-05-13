"""Definiuje wzorce adresów url dla news"""
from django.urls import path
from . import views

app_name = 'news'
urlpatterns = [
    #Strona główna
    path('', views.index, name='index'),
]