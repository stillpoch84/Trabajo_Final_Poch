from django.test import TestCase

from app_inostri.models import Vino

class VinoTest(TestCase):
    def test_creacion_vino_1(self):
        vino = Vino(nombre='Chateau Vieux', bodega='Lopez', varietal='malbec', cosecha='2020', zona='Cafayate', provincia='Salta')
        vino.save()

        self.assertEqual(Vino.objects.count(), 1)
        self.assertIsNone(vino.id)

    def test_creacion_vino_2(self):
        with self.assertRaises(ValueError):
            vino = Vino(nombre='Chateau Vieux', bodega='Lopez', varietal='malbec', cosecha='viejo', zona='Cafayate', provincia='Salta')
            vino.save()
        self.assertEqual(Vino.objects.count(), 0)

