from django.contrib import admin
from django.urls import path

   
from app_inostri.views import BuscarVinoView, VinoListView, VinoCreateView, VinoDetailView, \
    VinoUpdateView, VinoDeleteView, BodegaListView, BodegaCreateView, BodegaDetailView, \
    BodegaUpdateView, BodegaDeleteView, BuscarBodegaView, VarietalListView, VarietalCreateView, VarietalDetailView, \
    VarietalUpdateView, VarietalDeleteView, BuscarVarietalView


urlpatterns = [
    path('vinos/', VinoListView.as_view(), name='lista_vinos'),
    path('crear-vino/', VinoCreateView.as_view(), name='crear_vino'),
    path('buscar-vino/', BuscarVinoView.as_view(), name='buscar_vino'),
    path('vinos/<int:pk>/', VinoDetailView.as_view(), name='ver_vino'),
    path('editar-vino/<int:pk>/', VinoUpdateView.as_view(), name="editar_vino"),
    path('eliminar-vino/<int:pk>/', VinoDeleteView.as_view(), name="eliminar_vino"), 
    path('bodegas/', BodegaListView.as_view(), name='lista_bodegas'),
    path('crear-bodega/', BodegaCreateView.as_view(), name='crear_bodega'),
    path('buscar-bodega/', BuscarBodegaView.as_view(), name='buscar_bodega'),
    path('bodegas/<int:pk>/', BodegaDetailView.as_view(), name='ver_bodega'),
    path('editar-bodega/<int:pk>/', BodegaUpdateView.as_view(), name="editar_bodega"),
    path('eliminar-bodega/<int:pk>/', BodegaDeleteView.as_view(), name="eliminar_bodega"), 
    path('varietales/', VarietalListView.as_view(), name='lista_varietales'),
    path('crear-varietal/', VarietalCreateView.as_view(), name='crear_varietal'),
    path('buscar-varietal/', BuscarVarietalView.as_view(), name='buscar_varietal'),
    path('varietales/<int:pk>/', VarietalDetailView.as_view(), name='ver_varietal'),
    path('editar-varietal/<int:pk>/', VarietalUpdateView.as_view(), name="editar_varietal"),
    path('eliminar-varietal/<int:pk>/', VarietalDeleteView.as_view(), name="eliminar_varietal"), 
    
]
