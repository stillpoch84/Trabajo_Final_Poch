from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='app_inostri/index.html',
        context=contexto,
    )
    return http_response