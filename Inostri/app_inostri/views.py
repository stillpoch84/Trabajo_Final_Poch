from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.

from app_inostri.forms import VinoFormulario


def listar_vinos(request):
    context = {
        'vino': Vino.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='app_inostri/lista_vinos.html',
        context=context
    )
    return http_response