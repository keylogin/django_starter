from django.shortcuts import render
from django.http import HttpResponse
import json
import urllib.request
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def get_weather_data(city, api_key):
    try:
        source = urllib.request.urlopen(
            f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}').read()
        data = json.loads(source)
        return data
    except Exception as e:
        logging.error(f"Error: {e}")
        return None

def extract_weather_data(data):
    try:
        weather_data = {
            "country_code": data.get('sys', {}).get('country'),
            "coordinate": f"{data.get('coord', {}).get('lon')} {data.get('coord', {}).get('lat')}",
            "temp": data.get('main', {}).get('temp'),
            "pressure": data.get('main', {}).get('pressure'),
            "humidity": data.get('main', {}).get('humidity'),
        }
        return weather_data
    except Exception as e:
        logging.error(f"Error: {e}")
        return None

def index(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        if city is None:
            return HttpResponse("Error: City not specified")
        api_key = 'd847857f0c661d56b5b2379b41f02a5e'  # replace with your actual API key
        data = get_weather_data(city, api_key)
        if data:
            weather_data = extract_weather_data(data)
            if weather_data:
                print(weather_data)
                return render(request, 'first_app/index.html', weather_data)
            else:
                return HttpResponse("Error: Unable to extract weather data")
        else:
            return HttpResponse("Error: Unable to retrieve weather data")
    else:
        return render(request, 'first_app/index.html', {})