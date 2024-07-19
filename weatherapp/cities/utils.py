import redis, re
from django.conf import settings

r = redis.StrictRedis(host = settings.REDIS_HOST,
                port = settings.REDIS_PORT,
                db = settings.REDIS_DB)

def get_cities_views(reverse):
    keys = r.scan_iter('cities:*:views')
    pattern = re.compile(r'cities:(.*):views')
    
    response = {}
    for key in keys:
        match = pattern.match(key.decode('utf-8'))
        if match:
            city_name = match.group(1)  # Extract the city name
            city_views = r.get(key).decode('utf-8')        
        
        response[city_name] = city_views
    
    response = {key: response[key] for key in sorted(response,
                                                     key = lambda item: response[item],
                                                     reverse = reverse)}
    return response
