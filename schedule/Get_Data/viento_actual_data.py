from functions.funciones import get_driver, get_lista
import json
import os
from datetime import datetime
import pytz

region= pytz.timezone('Europe/London')

# Creamos la variable de entorno para Docker
URL1= os.getenv('VIENTO_ACTUAL1')
URL2= os.getenv('VIENTO_ACTUAL2')

# Creamos la función para crear los objetos de nuestra API
async def dataObject(viento, direction, grados, update):
    obj_Data={ 'viento':viento, 'direccion':direction, 'grados': grados, 'update': update}
    return obj_Data


async def get_Data_viento_actual():

    driver1= await (get_driver(URL1))
    print('Driver 1 ',driver1)
    driver2= await get_driver(URL2)
    print('Driver 2 ',driver2)
    print('scraping driver 1')
    direccionVientoActual= driver1.find_elements('xpath','//*[@id="spot-data"]/div[2]/span[1]/span')
    print('scraping driver 2')
    gradosVientoActual=  driver1.find_elements('xpath','//*[@id="spot-data"]/div[2]/span[2]/span')

    vientoActual =  driver2.find_elements('xpath','/html/body/header/v[1]/span')

    hora= datetime.now(region).hour
    minutos= datetime.now().minute
    vientoList= get_lista(vientoActual)
    directionList= get_lista( direccionVientoActual)
    gradosList= get_lista(gradosVientoActual)
    gradosList= list(map(lambda str: str.replace('°', ''),gradosList))  
    updateList= f'Ultima actualización: {hora}:{minutos}'
    apiActualWind= await dataObject(vientoList, directionList, gradosList, [updateList])
    print('dataObject', apiActualWind)
    
    try:
        with open('data/apiActualWind.json', 'w') as file:
            print('Escribiendo apiActualWind...')
            try:
                json.dump(apiActualWind, file)
            except:
                print('No hemos podido escribir el archivo')   
    except:
        print('No podemos escribir...', apiActualWind)   


    driver1.quit()
    driver2.quit()

    return await file


 
