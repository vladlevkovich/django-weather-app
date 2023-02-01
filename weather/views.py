from django.shortcuts import render
from .services import services


def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = None

    return render(request, 'weather/weather.html', services.get_weather(city=city))


