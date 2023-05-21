from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Articulo
from datetime import date

from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Articulo
from django.contrib.auth.mixins import LoginRequiredMixin
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class CrearPostView(LoginRequiredMixin, CreateView):
    model = Articulo
    fields = ('titulo', 'subtitulo', 'cuerpo', 'imagen')
    success_url = reverse_lazy('lista_posts')  # Specify the URL to redirect after successful form submission

    def form_valid(self, form):
        form.instance.autor = self.request.user  # Set the autor field to the logged-in user
        form.instance.fecha = date.today()  # Set the fecha field to today's date
        return super().form_valid(form)
        
    
class PostListView(ListView):
    model = Articulo
    template_name = 'lista_posts'
    context_object_name = 'articulos'

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Articulo
    success_url = reverse_lazy('lista_posts')