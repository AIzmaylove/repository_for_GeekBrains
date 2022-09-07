from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate
from .views import AuthorModelViewSet
from django.contrib.auth.models import User


class AuthorTestCase(TestCase):

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/authors/')
        view = AuthorModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_get_list_1(self):
        factory = APIRequestFactory()
        request = factory.get('/api/authors/')
        user = User.objects.create_superuser(username='DRF_0', password='geekbrains')
        force_authenticate(request, user=user)
        view = AuthorModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# Create your tests here.
