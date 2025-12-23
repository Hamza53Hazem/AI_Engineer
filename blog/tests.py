from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Category
from rest_framework.test import APIClient
from rest_framework import status

class BlogApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.category = Category.objects.create(name='Tech')
        self.post = Post.objects.create(
            title='Test Post',
            content='Content',
            author=self.user,
            category=self.category,
            status='published'
        )

    def test_get_users(self):
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_posts(self):
        response = self.client.get(reverse('post-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Post')

