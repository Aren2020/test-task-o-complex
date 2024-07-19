import requests, json, redis
from geopy.geocoders import Nominatim
from datetime import datetime
from django.conf import settings

r = redis.StrictRedis(host = settings.REDIS_HOST,
                port = settings.REDIS_PORT,
                db = settings.REDIS_DB)

class Weather:

    def get_lat_long(self, city):
        geolocator = Nominatim(user_agent = "Weather App")
        location = geolocator.geocode(city)
        if location:
            return location.latitude, location.longitude
        else:
            return None, None

    def get_weather(self, city):
        lat, long = self.get_lat_long(city)
        params = {
            'latitude': lat,
            'longitude': long,
            'timezone': 'auto',
            'current': 'temperature_2m,wind_speed_10m',
            'hourly': 'temperature_2m,relative_humidity_2m,wind_speed_10m'
        }
    
        url = 'https://api.open-meteo.com/v1/forecast'
        response = requests.get(url, params = params)
        try:
            response = self.data_format( response.json() )
            r.incr(f'cities:{city}:views')
        except json.JSONDecodeError:
            response = 'That city is not available in our application'
        return response

    def get_day_of_week(self, date):
        date_obj = datetime.fromisoformat(date)
        return date_obj.strftime("%A")


    def data_format(self, data):
        response = {}
        date_list = data['hourly']['time']
        for i, date_str in enumerate(date_list):
            date, time = date_str.split('T')
            day_of_week = self.get_day_of_week(date_str)
            
            part = {time: {
                        'wind_speed_10m': f'{ data["hourly"]["wind_speed_10m"][i] } km/h',
                        'relative_humidity_2m': f'{ data["hourly"]["relative_humidity_2m"][i] } %',
                        'temperature_2m': f'{ data["hourly"]["temperature_2m"][i] } °C',
                    }}
            
            if not response.get(day_of_week):
                response[day_of_week] = part
            else:
                response[day_of_week].update(part)

        return response
    