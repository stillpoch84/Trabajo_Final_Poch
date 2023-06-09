from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from blog_inostri.views import CrearPostView, PostListView, PostDetailView, PostDeleteView, PostUpdateView

urlpatterns = [
path('posts/', PostListView.as_view(), name='lista_posts'),
path('crear-post/', CrearPostView.as_view(), name='crear_post'),
path('posts/<int:pk>/', PostDetailView.as_view(), name='ver_post'),
path('eliminar-post/<int:pk>/', PostDeleteView.as_view(), name='eliminar_post'),
path('editar-post/<int:pk>/', PostUpdateView.as_view(), name='editar_post'),
path('ckeditor/', include('ckeditor_uploader.urls')),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)