from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

 

class Articulo(models.Model):
    titulo = models.CharField(max_length=128)
    subtitulo = models.CharField(max_length=256)
    cuerpo = RichTextField(default="")
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(blank=True, null=True)

    def __str__(self):
        return f'{self.titulo} | {self.subtitulo} | {self.cuerpo} |  {self.imagen}'

def save(self, *args, **kwargs):
    if not self.id:  
            self.autor = self.autor = self.request.user
    super(Articulo, self).save(*args, **kwargs)