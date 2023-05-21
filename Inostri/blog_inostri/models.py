from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

 

class Articulo(models.Model):
    titulo = models.CharField(max_length=128)
    subtitulo = models.CharField(max_length=256)
    cuerpo = RichTextField(default="")
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=False)
    imagen = models.ImageField(upload_to='articulo_images/', blank=True, null=True)

    def __str__(self):
        return f'{self.titulo} | {self.subtitulo} | {self.cuerpo} | {self.autor}'

def save(self, *args, **kwargs):
    if not self.id:  # Check if the object is being created (not updated)
            # Set the autor field to the logged-in user
            #self.autor = User.objects.get(username='username')  # Replace 'current_user' with the appropriate way to access the logged-in user
            self.autor = self.autor = self.request.user
    super(Articulo, self).save(*args, **kwargs)