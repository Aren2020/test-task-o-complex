from django.contrib import admin
from django.urls import path, include
from weather import views

urlpatterns = [
    path('', views.weather_redirect, name = 'home_redirect'),
    path('cities/', include('cities.urls', namespace = 'cities')),
    path('search/', include('search.urls', namespace = 'search')),
    path('weather/', include('weather.urls', namespace = 'weather')),
    path('admin/', admin.site.urls),
]