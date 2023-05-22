from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django import forms
# from .models import Bodega, Vino, Varietal

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
        object_list = Vino.objects.filter(Q(nombre__icontains=query)|Q(bodega__icontains=query)|Q(varietal__icontains=query)|Q(zona__icontains=query)|Q(provincia__icontains=query))
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
    # template_name = 'app_inostri/formulario_varietal.html'
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
    
