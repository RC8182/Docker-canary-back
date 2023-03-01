from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
import os

# Creamos la variable de entorno para Docker
URL1= os.getenv('VIENTO_ACTUAL1')
URL2= os.getenv('VIENTO_ACTUAL2')

    # Creamos una función para iterar sobre la info pedida y almazenarla en una lista
def get_lista(list):
    lista=[]
    for i in range(len(list)):
        lista.append(list[i].text)  
    return lista
        # Creamos la función para crear los objetos de nuestra API
def dataObject(viento, direction, grados):
    obj_Data={ 'viento':viento, 'direccion':direction, 'grados': grados}
    return obj_Data


def get_scrapt(url, path):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=chrome_options)
    driver.get(url)
    time.sleep(2)
    scrapt= driver.find_elements('xpath',path)

    return scrapt


def scrap_Data_viento_actual():

    direccionVientoActual= get_scrapt(URL1,'//*[@id="spot-data"]/div[2]/span[1]/span')
    gradosVientoActual= get_scrapt(URL1,'//*[@id="spot-data"]/div[2]/span[2]/span')

    vientoActual = get_scrapt(URL2,'/html/body/header/v[1]/span')

            
    vientoList= get_lista(vientoActual)
    directionList= get_lista(direccionVientoActual)
    gradosList= get_lista(gradosVientoActual)
    gradosList= list(map(lambda str: str.replace('°', ''), gradosList))  
    apiActualWind= dataObject(vientoList, directionList, gradosList)

    
    
    with open('data/apiActualWind.json', 'w') as api_Actual_Wind:
        try:
            json.dump(apiActualWind, api_Actual_Wind)
        except:
            print('No hemos podido escribir el archivo')    

    return api_Actual_Wind


 
