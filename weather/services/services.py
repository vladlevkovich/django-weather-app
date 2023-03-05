from .key import api_key
import requests
import datetime
import math


def get_weather(city):
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q': city, 'appid': api_key, 'lang': 'ua'}
    r = requests.get(url=URL, params=PARAMS)

    if r.status_code == 200:
        data = r.json()
        description = data['weather'][0]['description']
        temp = math.floor(data['main']['temp'] - 273)
        temp_min = math.floor(data['main']['temp_min'] - 273)
        temp_max = math.floor(data['main']['temp_max'] - 273)
        icon = data['weather'][0]['icon']
        time_sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        time_sunset = datetime.datetime.fromtimestamp(data['sys']['sunset'])

        context = {
            'description': description, 'temp': temp, 'icon': icon, 'city': city, 'time_sunrise': time_sunrise, 'time_sunset': time_sunset, 'temp_min': temp_min, 'temp_max': temp_max

        }
        return context


