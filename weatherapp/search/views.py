from django.http import JsonResponse
from django.conf import settings

def search(request, query):
    cities = settings.CITIES
    matches = []
    for city in cities:
        if city.lower().startswith(query.lower()):
            matches.append(city)

    matches = list(set(matches)) # this is the problem of cities.txt this text doc have dublicates

    return JsonResponse({'matches': matches})