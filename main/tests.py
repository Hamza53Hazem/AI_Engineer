from django.test import TestCase
from django.urls import reverse

from .models import Service


class HomeViewTests(TestCase):
	def test_home_renders(self):
		response = self.client.get(reverse("home"))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, "main/home.html")


class ServiceModelTests(TestCase):
	def test_string_representation(self):
		service = Service.objects.create(title="Test", description="Details")
		self.assertEqual(str(service), "Test")
