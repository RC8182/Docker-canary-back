import requests
import json
import os

def get_mareas():
    url = os.getenv('MAREAS_DATA')
    headers = {'Accept': 'application/json',
               'Content-Type':'application/json'
               }
    response = requests.request('GET',url, headers=headers, data={})
    
    apiMareas= response.json()

    with open('data/apiMareas.json', 'w') as api_mareas:
        try:
            json.dump(apiMareas, api_mareas)
        except:
            print('No se ha podido escribir')    

    
    return api_mareas