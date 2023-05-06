from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.

from app_inostri.models import Vino, Bodega, Varietal
from app_inostri.forms import VinoFormulario 


def listar_vinos(request):
    context = {
        'vinos': Vino.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='app_inostri/lista_vinos.html',
        context=context
    )
    return http_response

def crear_vino(request):
    if request.method == 'POST':
        formulario = VinoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data 
            nombre = data['nombre']
            bodega = data['bodega']
            varietal = data['varietal']
            cosecha = data['cosecha']
            region = data['region']
            provincia = data['provincia']
            vino = Vino(nombre=nombre, bodega=bodega, varietal=varietal, cosecha=cosecha, region=region, provincia=provincia)
            vino.save()

            url_exitosa = reverse('lista_vinos')
            return redirect(url_exitosa)
        else:
            formulario = VinoFormulario()
        http_response = render(
            request=request,
            template_name='app_inostri/formulario_vino.html',
            context={'formulario': formulario}
        )
        return http_response  

def buscar_vino(request):
    if request.method == 'POST':
        data = request.POST
        busqueda = data['busqueda']
        vinos = Vino.objects.filter(nombre__contains=busqueda)
        context = {
            'vinos': vinos,
        }
        http_response = render(
            request=request,
            template_name='app_inostri/lista_vinos.html',
            context=context,
        )
        return http_response
    

def listar_bodegas(request):
    context = {
        'bodegas': Bodega.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='app_inostri/lista_bodegas.html',
        context=context
    )
    return http_response

def listar_varietales(request):
    context = {
        'varietales': Varietal.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='app_inostri/lista_varietal.html',
        context=context
    )
    return http_response