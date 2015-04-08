from django.core.urlresolvers import reverse
from django.test import TestCase
from models import *
from django.contrib.auth.models import User
# Create your tests here.
#Prueba de funciones logicas
class SimpleTest(TestCase):
	def setUp(self):
		self.categoria = Categoria.objects.create(titulo="categoria de pruebas")
		self.usuario = User.objects.create_user(username="gato",password="maldito")
	def test_es_popular(self):
		#si una catecoria tiene menos de 11 botos no es test_es_popular
		#si un enlace tiene mas de 10 botos es test_es_populas

		enlace = Enlace.objects.create(
			titulo = 'Prueba',
			enlace = 'https:""google.com',
			categoria = self.categoria, usuario = self.usuario,
		)
		self.assertEqual(enlace.votos,0)
		self.assertEqual(enlace.es_popular(),False)
		self.assertFalse(enlace.es_popular())
		#si el enlace tiene mas de 11 votos no es es_popular
		enlace.votos = 20
		enlace.save()

		self.assertEqual(enlace.votos,20)
		self.assertEqual(enlace.es_popular(),True)
		self.assertTrue(enlace.es_popular())
	def test_views(self):
		res = self.client.get(reverse('home'))
		self.assertEqual(res.status_code,200)
		self.client.login(username="gato",password="maldito")
		res = self.client.get(reverse('add'))
		self.assertEqual(res.status_code,200)

	def test_add(self):
		self.client.login(username="gato",password="maldito")
		self.assertEqual(Enlace.objects.count(),0)
		data = {} #DECLARAR DICCIONARIO
		data['titulo'] = 'test titulo'
		data['enlace'] = 'http://www.google.com/'
		data['categoria'] = self.categoria.id
		res = self.client.post(reverse('add'),data)
		self.assertEqual(res.status_code,302)
		self.assertEqual(Enlace.objects.count(),1)

		enlace = Enlace.objects.all()[0]
		self.assertEqual(enlace.titulo,data['titulo'])
		self.assertEqual(enlace.categoria.id,data['categoria'])
		self.assertEqual(enlace.enlace,data['enlace'])
		