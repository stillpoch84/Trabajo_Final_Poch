
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from sistema_inostri.views import inicio



urlpatterns = [
    path('', inicio, name='inicio'),
    path('admin/', admin.site.urls),
    path('inostri/', include("app_inostri.urls")),
    path("perfiles/", include("perfiles.urls")),
    path('inostri-blog/', include('blog_inostri.urls')),
#    path('ckeditor/', include('ckeditor_uploader.urls')),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)