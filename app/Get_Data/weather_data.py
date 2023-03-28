import requests
import json
from datetime import datetime
import os

def get_weather():
    updated= str(datetime.now())
    URL = os.getenv('WEATHER_DATA')
    headers = {'Accept': 'application/json',
               'Content-Type':'application/json'
               }
    response = requests.request('GET',URL, headers=headers, data={})
    
    apiWeather= [{'last_update': updated},response.json()]
    try:
        with open('data/apiWeather.json', 'w') as file:
            print('Escribiendo apiWeather...')
            try:
                json.dump(apiWeather, file)
            except:
                print('No se ha podido escribir') 

    except:
        print('Error apiWeather...')    
   
    return file