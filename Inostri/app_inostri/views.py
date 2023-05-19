from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django import forms
from .models import Bodega, Vino

from app_inostri.models import Vino, Bodega, Varietal

class VinoListView(ListView):
    model = Vino
    template_name = 'app_inostri/lista_vinos.html'

class VinoCreateView(LoginRequiredMixin, CreateView):
    model = Vino
    fields = ('nombre', 'bodega', 'varietal', 'cosecha', 'zona', 'provincia')
    success_url = reverse_lazy('lista_vinos')

class VinoDetailView(LoginRequiredMixin, DetailView):
    model = Vino
    success_url = reverse_lazy('lista_vinos')

class VinoUpdateView(LoginRequiredMixin, UpdateView):
    model = Vino
    fields = ('nombre', 'bodega', 'varietal', 'cosecha', 'zona', 'provincia')
    success_url = reverse_lazy('lista_vinos')

class VinoDeleteView(LoginRequiredMixin, DeleteView):
    model = Vino
    success_url = reverse_lazy('lista_vinos')

class BuscarVinoView(ListView):
    model = Vino
    template_name = 'app_inostri/buscar_vino.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Vino.objects.filter(Q(nombre__icontains=query)|Q(bodega__icontains=query)|Q(Varietal__icontains=query)|Q(zona__icontains=query)|Q(provincia__icontains=query))
        return object_list


class BodegaListView(ListView):
    model = Bodega
    template_name = 'app_inostri/lista_bodegas.html'

class BodegaCreateView(LoginRequiredMixin, CreateView):
    model = Bodega
    fields = ('nombre', 'direccion', 'zona', 'provincia', 'telefono', 'email')
    success_url = reverse_lazy('lista_bodegas')

class BodegaDetailView(LoginRequiredMixin, DetailView):
    model = Bodega
    success_url = reverse_lazy('lista_bodegas')

class BodegaUpdateView(LoginRequiredMixin, UpdateView):
    model = Bodega
    fields = ('nombre', 'direccion', 'zona', 'provincia', 'telefono', 'email')
    success_url = reverse_lazy('lista_bodegas')

class BodegaDeleteView(LoginRequiredMixin, DeleteView):
    model = Bodega
    success_url = reverse_lazy('lista_bodegas')

class BuscarBodegaView(ListView):
    model = Bodega
    template_name = 'app_inostri/buscar_bodega.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Bodega.objects.filter(Q(nombre__icontains=query)|Q(provincia__icontains=query)|Q(zona__icontains=query))
        return object_list

class VarietalListView(ListView):
    model = Varietal
    template_name = 'app_inostri/lista_varietales.html'

class VarietalCreateView(LoginRequiredMixin, CreateView):
    model = Varietal
    fields = ('nombre', 'descripcion')
    success_url = reverse_lazy('lista_varietales')

class VarietalDetailView(LoginRequiredMixin, DetailView):
    model = Varietal
    success_url = reverse_lazy('lista_varietales')

class VarietalUpdateView(LoginRequiredMixin, UpdateView):
    model = Varietal
    fields = ('nombre', 'descripcion')
    success_url = reverse_lazy('lista_varietales')

class VarietalDeleteView(LoginRequiredMixin, DeleteView):
    model = Varietal
    success_url = reverse_lazy('lista_varietales')

class BuscarVarietalView(ListView):
    model = Varietal
    template_name = 'app_inostri/buscar_varietal.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Varietal.objects.filter(Q(nombre__icontains=query)|Q(descripcion__icontains=query))
        return object_list
    
def AboutUs(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='app_inostri/about_us.html',
        context=contexto,
    )
    return http_response
    
# def listar_vinos(request):
#     context = {
#         'vinos': Vino.objects.order_by('nombre'),
#     }
#     http_response = render(
#         request=request,
#         template_name='app_inostri/lista_vinos.html',
#         context=context
#     )
#     return http_response

# def crear_vino(request):
#     if request.method == 'POST':
#         formulario = VinoFormulario(request.POST)

#         if formulario.is_valid():
#             data = formulario.cleaned_data 
#             nombre = data['nombre']
#             bodega = data['bodega']
#             varietal = data['varietal']
#             cosecha = data['cosecha']
#             zona = data['zona']
#             provincia = data['provincia']
#             vino = Vino(nombre=nombre, bodega=bodega, varietal=varietal, cosecha=cosecha, zona=zona, provincia=provincia)
#             vino.save()

#             url_exitosa = reverse('lista_vinos')
#             return redirect(url_exitosa)
#     else:
#             formulario = VinoFormulario()
#     http_response = render(
#             request=request,
#             template_name='app_inostri/formulario_vino.html',
#             context={'formulario': formulario}
#         )
#     return http_response  

# def buscar_vino(request):
#     if request.method == 'POST':
#         data = request.POST
#         busqueda = data['busqueda']
#         vinos = Vino.objects.filter(nombre__contains=busqueda)
#         vinos = Vino.objects.filter(bodega__contains=busqueda)
#         context = {
#             'vinos': vinos,
#         }
#         http_response = render(
#             request=request,
#             template_name='app_inostri/lista_vinos.html',
#             context=context,
#         )
#         return http_response
    
# def eliminar_vino(request, id):
#    vino = Vino.objects.get(id=id)
#    if request.method == "POST":
#        vino.delete()
#        url_exitosa = reverse('lista_vinos')
#        return redirect(url_exitosa)

# def editar_vino(request, id):
#     vino = Vino.objects.get(id=id)
#     if request.method == "POST":
#         formulario = VinoFormulario(request.POST)

#         if formulario.is_valid():
#             data = formulario.cleaned_data
#             vino.nombre = data['nombre']
#             vino.bodega = data['bodega']
#             vino.varietal = data['varietal']
#             vino.cosecha = data['cosecha']
#             vino.region = data['region']
#             vino.provincia = data['provincia']
#             vino.save()

#             url_exitosa = reverse('lista_vino')
#             return redirect(url_exitosa)
#     else:  # GET
#         inicial = {
#             'nombre': vino.nombre,
#             'bodega': vino.bodega,
#             'varietal': vino.varietal,
#             'cosecha': vino.cosecha,
#             'region': vino.region,
#             'provincia': vino.provincia,

#         }
#         formulario = VinoFormulario(initial=inicial)
#     return render(
#         request=request,
#         template_name='app_inostri/formulario_vino.html',
#         context={'formulario': formulario},
#     )
   

# def listar_bodegas(request):
#     context = {
#         'bodegas': Bodega.objects.all(),
#     }
#     http_response = render(
#         request=request,
#         template_name='app_inostri/lista_bodegas.html',
#         context=context
#     )
#     return http_response


# def buscar_bodega(request):
#     if request.method == 'POST':
#         data = request.POST
#         busqueda = data['busqueda']
#         bodegas = Bodega.objects.filter(nombre__contains=busqueda)
#         bodegas = Bodega.objects.filter(provincia__contains=busqueda)
#         context = {
#             'bodegas': bodegas,
#         }
#         http_response = render(
#             request=request,
#             template_name='app_inostri/lista_bodegas.html',
#             context=context,
#         )
#         return http_response 
    
# def crear_bodega(request):
#     if request.method == 'POST':
#         formulario = BodegaFormulario(request.POST)

#         if formulario.is_valid():
#             data = formulario.cleaned_data 
#             nombre = data['nombre']
#             direccion = data['direccion']
#             zona = data['zona']
#             provincia = data['provincia']
#             telefono = data['telefono']
#             email = data['email']
#             bodega = Bodega(nombre=nombre, direccion=direccion, region=region, provincia=provincia, telefono=telefono, email=email)
#             bodega.save()

#             url_exitosa = reverse('lista_bodegas')
#             return redirect(url_exitosa)
#     else:
#             formulario = BodegaFormulario()
#     http_response = render(
#             request=request,
#             template_name='app_inostri/formulario_bodega.html',
#             context={'formulario': formulario}
#         )
#     return http_response     

# def listar_varietales(request):
#     context = {
#         'varietales': Varietal.objects.order_by('nombre'),
#     }
#     http_response = render(
#         request=request,
#         template_name='app_inostri/lista_varietales.html',
#         context=context
#     )
#     return http_response

# def buscar_varietal(request):
#     if request.method == 'POST':
#         data = request.POST
#         busqueda = data['busqueda']
#         varietal = Varietal.objects.filter(nombre__contains=busqueda).order_by('nombre')
#         varietal = Varietal.objects.filter(descripcion__contains=busqueda).order_by('nombre')
#         context = {
#             'varietales': varietal,
#         }
#         http_response = render(
#             request=request,
#             template_name='app_inostri/lista_varietales.html',
#             context=context,
#         )
#         return http_response
    
# def crear_varietal(request):
#     if request.method == 'POST':
#         formulario = VarietalFormulario(request.POST)

#         if formulario.is_valid():
#             data = formulario.cleaned_data 
#             nombre = data['nombre']
#             descripcion = data['descripcion']
#             varietal = Varietal(nombre=nombre, descripcion=descripcion)
#             varietal.save()

#             url_exitosa = reverse('lista_varietales')
#             return redirect(url_exitosa)
#     else:
#             formulario = VarietalFormulario()
#     http_response = render(
#             request=request,
#             template_name='app_inostri/formulario_varietal.html',
#             context={'formulario': formulario}
#         )
#     return http_response  