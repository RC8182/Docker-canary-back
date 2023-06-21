import aiohttp
import json
from datetime import datetime
import os

async def get_weather():
    updated= str(datetime.now())
    URL = os.getenv('WEATHER_DATA')
    headers = {'Accept': 'application/json',
               'Content-Type':'application/json'
               }
    async with aiohttp.ClientSession() as session: 
        async with session.get(URL, headers=headers, data={}) as response: 
            
            apiWeather= [{'last_update': updated}, await response.json()]
    try:
        with open('./weather_data.py', 'w') as file:

            try:
                json.dump(apiWeather, file)
            except:
                print('No se ha podido escribir apiweather') 
    except:
        print('Error with Weather Data')
    return file