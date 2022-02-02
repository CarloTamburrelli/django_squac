from django.test import TestCase
from django.contrib.auth.models import User
from django.core import serializers
from django.http import JsonResponse
from django.urls import reverse
from users.models import Profile



class URLTests(TestCase):
	def test_testhomepage(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)

	def test_aboutpage(self):
		url = reverse('about')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'system/about.html')
		#self.assertContains(response, 'Company Name XYZ')

	def test_profilestroutput(self):
		user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
		user.save()
		prof = Profile.objects.get(pk=1)
		self.assertEqual(str(prof), f'{prof.user.username} Profile' )
