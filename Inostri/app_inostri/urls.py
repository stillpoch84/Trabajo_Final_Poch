from django.contrib import admin
from django.urls import path

from app_inostri import listar_vinos

urlpatterns = [
    path('vinos/', listar_vinos, name='lista_vinos'),
]
