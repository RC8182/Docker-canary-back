import aiohttp
import json
import os
from datetime import datetime

async def get_mareas():
    updated= str(datetime.now())
    URL = os.getenv('MAREAS_DATA')
    headers = {'Accept': 'application/json',
               'Content-Type':'application/json'
               }
    async with aiohttp.ClientSession() as session: 
        async with session.get(URL, headers=headers, data={}) as response: 
            
            apiMareas= [{'last_update': updated}, await response.json()]
    try:
        with open('data/apiMareas.json', 'w') as file:
            print('Escribiendo apiMareas...')
            try:
                json.dump(apiMareas, file)
            except:
                print('No se ha podido escribir')    
    except: 
        print('Error with open apiMareas')

    return file