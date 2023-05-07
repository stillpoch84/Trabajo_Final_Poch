from django.contrib import admin
from django.urls import path

from app_inostri.views import listar_vinos, listar_bodegas, listar_varietales, crear_vino, buscar_vino, buscar_varietal

urlpatterns = [
    path('vinos/', listar_vinos, name='lista_vinos'),
    path('crear-vinos/', crear_vino, name='crear_vino'),
    path('buscar-vino/', buscar_vino, name='buscar_vino'),
    path('bodegas/', listar_bodegas, name='lista_bodegas'),
    path('varietales/', listar_varietales, name='lista_varietales'),
    path('buscar-varietal/', buscar_varietal, name='buscar_varietal'),
]
