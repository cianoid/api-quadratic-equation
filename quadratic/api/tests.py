from django.urls import include, path
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient, APITestCase, URLPatternsTestCase


class APITests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/', include('api.urls')),
    ]

    client: APIClient
    equation_endpoint = reverse('api:equation')

    def setUp(self):
        self.client = APIClient()

    def test_two_roots_answer(self):
        """Тестирование ответа с двумя корнями (D > 0)."""

        data = {'a': 4, 'b': 21, 'c': 5}
        response = self.client.post(
            self.equation_endpoint, data=data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['roots_count'], 2)
        self.assertEqual(response.data['roots'], [-0.25, -5.0])

    def test_one_root_answer(self):
        """Тестирование ответа с одним корнем (D == 0)."""

        data = {'a': 1, 'b': 12, 'c': 36}
        response = self.client.post(
            self.equation_endpoint, data=data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['roots_count'], 1)
        self.assertEqual(response.data['roots'], [-6.0])

    def test_zero_roots_answer(self):
        """Тестирование ответа без корней (D < 0)."""

        data = {'a': 10, 'b': -2, 'c': 81}
        response = self.client.post(
            self.equation_endpoint, data=data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['roots_count'], 0)
        self.assertEqual(response.data['roots'], [])

    def test_error_if_no_parameters_passed(self):
        """Тестирование ответа, если не переданы параметры."""

        response = self.client.post(
            self.equation_endpoint, data={}, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        for key in ['a', 'b', 'c']:
            with self.subTest(parameter=key):
                self.assertEqual(
                    str(response.data[key][0]), 'Обязательное поле.')

    def test_error_if_a_is_zero(self):
        """Тестирование ответа, если a == 0."""

        data = {'a': 0, 'b': 10, 'c': 3}
        response = self.client.post(
            self.equation_endpoint, data=data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data['a'][0], 'Параметр не может быть равен 0')
