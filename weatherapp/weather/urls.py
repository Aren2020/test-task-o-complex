from django.urls import path
from . import views

app_name = 'weather'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('<city>/', views.city, name = 'city'),
]