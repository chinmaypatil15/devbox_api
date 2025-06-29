from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class DevboxAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='admin', password='password')
        self.token, _ = Token.objects.get_or_create(user=self.user)
        self.auth_headers = {'HTTP_AUTHORIZATION': f'Token {self.token.key}'}

    def test_login_success(self):
        response = self.client.post('/api/login/', {'username': 'admin', 'password': 'password'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_profile_authenticated(self):
        response = self.client.get('/api/profile/', **self.auth_headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('username', response.data)

    def test_profile_unauthenticated(self):
        response = self.client.get('/api/profile/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_api_usage(self):
        response = self.client.get('/api/api-usage/', **self.auth_headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_api_usage(self):
        data = {'endpoint': '/test', 'method': 'POST', 'timestamp': '2025-06-29T12:00:00Z'}
        response = self.client.post('/api/api-usage/', data, **self.auth_headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['status'], 'added')