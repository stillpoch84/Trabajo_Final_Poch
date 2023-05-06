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
        'vinos': Varietal.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='app_inostri/lista_varietal.html',
        context=context
    )
    return http_response