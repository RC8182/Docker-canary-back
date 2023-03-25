import requests
import json
import os

def get_weather():
    URL = os.getenv('WEATHER_DATA')
    headers = {'Accept': 'application/json',
               'Content-Type':'application/json'
               }
    response = requests.request('GET',URL, headers=headers, data={})
    
    apiWeather= response.json()

    with open('data/apiWeather.json', 'w') as api_weather:
        try:
            json.dump(apiWeather, api_weather)
        except:
            print('No se ha podido escribir')    

    
    return api_weather