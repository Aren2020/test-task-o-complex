import json
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .utils import Weather

def weather_redirect(request):
    return redirect('weather:home')

def home(request):
    return render(request, 'weather/home.html')

def city(request, city):
    weather = Weather()
    weather_info = weather.get_weather(city)
    response = render(request, 'weather/home.html',
                      context = {'weather_info': json.dumps(weather_info)})
    response.set_cookie('city', city)
    return response
