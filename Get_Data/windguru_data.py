from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import json




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


def scrap_Data_windguru():
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.windguru.cz/station/3209")

    time.sleep(2)

    vientoActual = driver.find_elements('xpath','//*[@id="spot-data"]/div[3]/a/span[1]')
    direccionVientoActual= driver.find_elements('xpath','//*[@id="spot-data"]/div[2]/span[1]/span')
    gradosVientoActual= driver.find_elements('xpath','//*[@id="spot-data"]/div[2]/span[2]/span')
        
    
    vientoList= get_lista(vientoActual)
    directionList= get_lista(direccionVientoActual)
    gradosList= get_lista(gradosVientoActual)
    gradosList= list(map(lambda str: str.replace('°', ''), gradosList))  
    apiActualWind= dataObject(vientoList, directionList, gradosList)

    with open('apiActualWind.json', 'w') as api:
        json.dump(apiActualWind, api)

    driver.quit()

    return api


 
