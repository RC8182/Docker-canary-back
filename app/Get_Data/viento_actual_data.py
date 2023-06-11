from functions.funciones import get_driver, get_lista
import json
import os
import time

# Creamos la variable de entorno para Docker
URL1= os.getenv('VIENTO_ACTUAL1')
URL2= os.getenv('VIENTO_ACTUAL2')

# Creamos la función para crear los objetos de nuestra API
def dataObject(viento, direction, grados):
    obj_Data={ 'viento':viento, 'direccion':direction, 'grados': grados}
    return obj_Data


def get_Data_viento_actual():
    driver1= get_driver(URL1)
    driver2= get_driver(URL2)

    direccionVientoActual= driver1.find_elements('xpath','//*[@id="spot-data"]/div[2]/span[1]/span')
    gradosVientoActual=  driver1.find_elements('xpath','//*[@id="spot-data"]/div[2]/span[2]/span')

    vientoActual =  driver2.find_elements('xpath','/html/body/header/v[1]/span')

            
    vientoList= get_lista(vientoActual)
    directionList= get_lista(direccionVientoActual)
    gradosList= get_lista(gradosVientoActual)
    gradosList= list(map(lambda str: str.replace('°', ''), gradosList))  
    apiActualWind= dataObject(vientoList, directionList, gradosList)
    
    with open('data/apiActualWind.json', 'w') as file:
        print('Escribiendo apiActualWind...')
        try:
            json.dump(apiActualWind, file)
        except:
            print('No hemos podido escribir el archivo')   
             
    time.sleep(2)
    driver1.quit()
    driver2.quit()
    return file


 
