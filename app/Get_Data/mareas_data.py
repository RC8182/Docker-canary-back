import requests
import json
import os
from datetime import datetime

def get_mareas():
    updated= str(datetime.now())
    URL = os.getenv('MAREAS_DATA')
    headers = {'Accept': 'application/json',
               'Content-Type':'application/json'
               }
    response = requests.request('GET',URL, headers=headers, data={})
    
    apiMareas= [{'last_update': updated}, response.json()]
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