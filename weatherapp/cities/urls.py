from django.urls import path
from . import views

app_name = 'cities'

urlpatterns = [
    path('views/', views.cities_views, name ='views'),
]