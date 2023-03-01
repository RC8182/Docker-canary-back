import requests
import json

def get_mareas():
    url = 'https://ideihm.covam.es/api-ihm/getmarea?request=gettide&id=64&format=json&month=202303'
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