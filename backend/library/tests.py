import random
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient
from .models import Author
from .views import AuthorModelViewSet
from users.models import CustomUser
from mixer.backend.django import mixer

class AuthorTestCase(TestCase):

    def setUp(self) -> None:
        self.user = CustomUser.objects.create_superuser(username='DRF_0', password='geekbrains')
        # self.author = Author.objects.create(first_name='Игорь', last_name='Губерман', birthday_year=1936)
        self.author = mixer.blend(Author, birthday_year=mixer.sequence(lambda c: int(random.random() * 2000)))


    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/authors/')
        view = AuthorModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_list_1(self):
        factory = APIRequestFactory()
        request = factory.get('/api/authors/')
        force_authenticate(request, user=self.user)
        view = AuthorModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)



class AuthorClientTestCase(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = CustomUser.objects.create_superuser(username='DRF_0', password='geekbrains')
        self.author = Author.objects.create(first_name='Игорь', last_name='Губерман', birthday_year=1936)

    def test_get_list(self):
        response = self.client.get('/api/authors/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_list_1(self):
        self.client.force_authenticate(self.user)
        response = self.client.get('/api/authors/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_list_2(self):
        self.client.login(username='DRF_0', password='geekbrains')
        response = self.client.get('/api/authors/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.client.logout()
        response = self.client.get('/api/authors/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post(self):
        self.client.login(username='denis', password='qwerty')
        # self.client.force_login(user=self.user)
        response = self.client.post('/api/authors/', {
            "first_name": "Сергей",
            "last_name": "Довлатов",
            "birthday_year": 1941
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        author = Author.objects.get(pk=response.data.get('id'))
        self.assertEqual(author.last_name, 'Довлатов')