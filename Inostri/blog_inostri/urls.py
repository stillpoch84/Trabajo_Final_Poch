from django.contrib import admin
from django.urls import path

from blog_inostri.views import CrearPostView, PostListView, PostDetailView

urlpatterns = [
path('posts/', PostListView.as_view(), name='lista_posts'),
path('crear-post/', CrearPostView.as_view(), name='crear_post'),
path('posts/<int:pk>/', PostDetailView.as_view(), name='ver_post'),

]