from django.test import TestCase, Client
from django.urls import reverse

class TestGetCitiesViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('cities:views')

    def test_get_cities_views(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
