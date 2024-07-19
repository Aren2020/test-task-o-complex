from django.http import JsonResponse
from .utils import get_cities_views

def cities_views(request):
    reverse = int(request.GET.get('reverse', 0))
    response = get_cities_views(reverse)
    return JsonResponse(response)
