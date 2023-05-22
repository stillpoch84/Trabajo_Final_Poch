from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Articulo
from datetime import date
from django.utils import timezone

from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Articulo
from django.contrib.auth.mixins import LoginRequiredMixin

class CrearPostView(LoginRequiredMixin, CreateView):
    model = Articulo
    fields = ('titulo', 'subtitulo', 'cuerpo', 'imagen')
    success_url = reverse_lazy('lista_posts')  

    def form_valid(self, form):
        form.instance.autor = self.request.user  
        form.instance.fecha = timezone.now().date()  
        form.instance.imagen = self.request.FILES.get('imagen')
        return super().form_valid(form)
        
    
class PostListView(ListView):
    model = Articulo
    template_name = 'lista_posts'
    context_object_name = 'articulos'
    ordering = ['-fecha']

class PostDetailView(DetailView):
    model = Articulo
    success_url = reverse_lazy('lista_posts')

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Articulo
    success_url = reverse_lazy('lista_posts')

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Articulo
    fields = ('titulo', 'subtitulo', 'cuerpo', 'imagen')
    success_url = reverse_lazy('lista_posts')   

    def form_valid(self, form):
        form.instance.autor = self.request.user
        form.instance.fecha = timezone.now().date()
        form.instance.imagen = self.request.FILES.get('imagen')
        return super().form_valid(form)