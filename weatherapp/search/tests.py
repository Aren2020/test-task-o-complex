from django.test import TestCase
from django.urls import reverse
from django.conf import settings

settings.CITIES = [
    "Moscow",
    "Monoko",
    "New York",
]

class SearchViewTests(TestCase):

    def test_search_view(self):
        query = "mo"
        expected_matches = ["Moscow", "Monoko"]

        url = reverse('search:matches', kwargs = {'query': query})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('matches', data)
        self.assertEqual(set(data['matches']), set(expected_matches))

    def test_search_view_no_matches(self):
        query = "xyz"

        url = reverse('search:matches', kwargs = {'query': query})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('matches', data)
        self.assertEqual(data['matches'], [])
