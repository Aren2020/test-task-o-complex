from django.test import TestCase, Client
from django.urls import reverse

class WeatherViewsTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_weather_redirect(self):
        response = self.client.get(reverse('home_redirect'))
        self.assertRedirects(response, reverse('weather:home'))

    def test_home_view(self):
        response = self.client.get(reverse('weather:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'weather/home.html')

    def test_city_view(self):
        city_name = 'moscow'
        response = self.client.get(reverse('weather:city', kwargs = {'city': city_name}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'weather/home.html')
        self.assertEqual(response.cookies['city'].value, city_name)