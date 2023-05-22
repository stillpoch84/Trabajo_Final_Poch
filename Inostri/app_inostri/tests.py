from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from app_inostri.models import Bodega, Vino

class VinoCreateViewTest(TestCase):
    def setUp(self):
        self.url = reverse('crear_vino')
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.data = {
            'nombre': 'Test Vino',
            'bodega': 'Test Bodega',
            'varietal': 'Test Varietal',
            'cosecha': '2022',
            'zona': 'Test Zona',
            'provincia': 'Test Provincia',
        }

    def test_vino_create_view(self):
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('lista_vinos'))

       
        self.assertEqual(Vino.objects.count(), 1)
        vino = Vino.objects.first()
        self.assertEqual(vino.nombre, 'Test Vino')
        self.assertEqual(vino.bodega, 'Test Bodega')
    

    def test_vino_create_view_unauthenticated(self):
        self.client.logout()
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login') + '?next=' + self.url)



class BuscarBodegaViewTest(TestCase):
    def setUp(self):
        self.url = reverse('buscar_bodega')
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.bodega = Bodega.objects.create(
            nombre='Test Bodega',
            provincia='Test Provincia',
            zona='Test Zona'
        )

    def test_buscar_bodega_view(self):
        response = self.client.get(self.url, {'q': 'Test'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_inostri/buscar_bodega.html')
        self.assertContains(response, 'Test Bodega')  

    def test_buscar_bodega_view_no_results(self):
        response = self.client.get(self.url, {'q': 'Nonexistent'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_inostri/buscar_bodega.html')
        self.assertNotContains(response, 'Test Bodega')

