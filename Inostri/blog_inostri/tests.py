from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
from .models import Articulo

class CrearPostViewTest(TestCase):
    def setUp(self):
        self.url = reverse('crear_post')
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.data = {
            'titulo': 'Test Titulo',
            'subtitulo': 'Test Subtitulo',
            'cuerpo': 'Test Cuerpo',
            'imagen': 'test_image.jpg',
            
        }

    def test_crear_post_view(self):
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, 302)  
        self.assertRedirects(response, reverse('lista_posts'))

       
        self.assertEqual(Articulo.objects.count(), 1)
        post = Articulo.objects.first()
        self.assertEqual(post.titulo, 'Test Titulo')
        self.assertEqual(post.subtitulo, 'Test Subtitulo')
        

    def test_crear_post_view_unauthenticated(self):
        self.client.logout() 
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, 302)  
        self.assertRedirects(response, reverse('login') + '?next=' + self.url)



class PostListViewTest(TestCase):
    def setUp(self):
        self.url = reverse('lista_posts')
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        self.post1 = Articulo.objects.create(
            titulo='Post 1',
            subtitulo='Subtitulo 1',
            cuerpo='Cuerpo 1',
            imagen='image1.jpg',
            autor=self.user  # Set the autor field to the user
        )
        self.post2 = Articulo.objects.create(
            titulo='Post 2',
            subtitulo='Subtitulo 2',
            cuerpo='Cuerpo 2',
            imagen='image2.jpg',
            autor=self.user  # Set the autor field to the user
        )

    def test_post_list_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog_inostri/articulo_list.html')
        self.assertContains(response, 'Post 1')