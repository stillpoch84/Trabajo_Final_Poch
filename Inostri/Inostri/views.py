from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='control_estudios/index.html',
        context=contexto,
    )
    return http_response