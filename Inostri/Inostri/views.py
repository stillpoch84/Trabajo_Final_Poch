from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    context = {}
    http_response = render(
        request=request,
        template_name='app_inostri/index.html',
        context=context,
    )
    return http_response