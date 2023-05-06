from django.contrib import admin

# Register your models here.

from app_inostri.models import Vino, Bodega, Varietal

admin.site.register(Vino)
admin.site.register(Bodega)
admin.site.register(Varietal)
