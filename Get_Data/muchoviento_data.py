from selenium import webdriver
import os
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import json


#Viento Tablas en El Medano
def scrap_MuchoViento():
    time.sleep(1)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    driver.get("https://muchoviento.net/El%20M%C3%A9dano%20-%20Playa%20Sur/forecast72")

    time.sleep(2)

    tabla_Horas = driver.find_elements('xpath','//*[@id="tabelle"]/table[1]/tbody/tr[2]')

    ###   Día 1   ###

    tabla_dia_1= driver.find_elements('xpath', '//*[@id="tabelle"]/table[1]/tbody/tr[1]/th[2]')
    tabla_viento_dia1 = driver.find_elements('xpath','//*[@id="tabelle"]/table[1]/tbody/tr[3]')
    tabla_direccion_viento_dia1= driver.find_elements('xpath','//*[@id="tabelle"]/table[1]/tbody/tr[5]')
    tabla_racha_dia1 = driver.find_elements('xpath','//*[@id="tabelle"]/table[1]/tbody/tr[4]')
    tabla_temp_dia1 = driver.find_elements('xpath','//*[@id="tabelle"]/table[1]/tbody/tr[6]')


    ###   Día 2   ###
    tabla_dia_2= driver.find_elements('xpath', '//*[@id="tabelle"]/table[1]/tbody/tr[8]/th[2]')
    tabla_viento_dia2 = driver.find_elements('xpath','//*[@id="tabelle"]/table[1]/tbody/tr[10]')
    tabla_direccion_viento_dia2= driver.find_elements('xpath','//*[@id="tabelle"]/table[1]/tbody/tr[12]')
    tabla_racha_dia2 = driver.find_elements('xpath','//*[@id="tabelle"]/table[1]/tbody/tr[11]')
    tabla_temp_dia2 = driver.find_elements('xpath','//*[@id="tabelle"]/table[1]/tbody/tr[13]')

    ###   Día 3   ###
    tabla_dia_3= driver.find_elements('xpath', '//*[@id="tabelle"]/table[1]/tbody/tr[15]/th[2]')
    tabla_viento_dia3 = driver.find_elements('xpath','//*[@id="tabelle"]/table[1]/tbody/tr[17]')
    tabla_direccion_viento_dia3= driver.find_elements('xpath','//*[@id="tabelle"]/table[1]/tbody/tr[19]')
    tabla_racha_dia3 = driver.find_elements('xpath','//*[@id="tabelle"]/table[1]/tbody/tr[18]')
    tabla_temp_dia3 = driver.find_elements('xpath','//*[@id="tabelle"]/table[1]/tbody/tr[20]')


    

    # Creamos una función para iterar sobre la info pedida y almazenarla en una lista
    def get_lista(list):
        lista=[]
        for i in range(len(list)):
            lista.append(list[i].text)  
        return lista        

    # Creamos la función para crear los objetos de nuestra API
    def data(fecha, hora, temp, viento,fuerza, racha, direction):
        obj_Data={'fecha':fecha, 'hora': hora, 'temperatura':temp, 'viento':viento, 'fuerza':fuerza, 'racha':racha, 'direccion':direction}
        return obj_Data

    ################### Creamos una función para limpiar los datos  ########################

    
    def limpiarLista(lista, n):
        lista= get_lista(lista)
        listaLimpia= lista[0].split()
        for i in range(n):
            listaLimpia.pop(0)
        return listaLimpia

    # La lista viento llega con 2 valores, los indices pares son el viento y los impares la fuerza, creamos una función para separar Viento de Fuerza
    def filtrarViento(lista):
        viento=[]
        for i in range(len(lista)):
            if (int(i) % 2 == 0):
                viento.append(lista[i])
        return viento

    
    def filtrarFuerza(lista):
        fuerza=[]
        for i in range(len(lista)):
            if (int(i) % 2 != 0):
                fuerza.append(lista[i])
        return fuerza

 

    dia1= get_lista(tabla_dia_1)
    temp_D1= limpiarLista(tabla_temp_dia1, 2)
    viento_fuerza_D1= limpiarLista(tabla_viento_dia1, 2)
    viento_D1= filtrarViento(viento_fuerza_D1)
    fuerza_D1= filtrarFuerza(viento_fuerza_D1)
    dir_Viento_D1= limpiarLista(tabla_direccion_viento_dia1, 2)
    gusts_D1= limpiarLista(tabla_racha_dia1, 1)
    # comprobamos que que tenemos la misma cantidad de datos por hora 
    horasDiarias=24
    numeroDatos= len(temp_D1)
    diferencia_Datos_Horas= horasDiarias - numeroDatos + 1
    # igualamos la cantidad de datos con las horas eliminanda las horas sin datos
    hora_dia1= limpiarLista(tabla_Horas, diferencia_Datos_Horas)

    hora_dia2= limpiarLista(tabla_Horas, 1)
    hora_dia3= limpiarLista(tabla_Horas, 1)
    # Eliminamos la letra h de la lista hora
    # hora_dia1.translate("h", " ")
    # hora_dia2.replace("h", " ")
    # hora_dia3.replace("h", " ")
    # print(hora_dia1)

    dia2= get_lista(tabla_dia_2)
    temp_D2= limpiarLista(tabla_temp_dia2, 2)
    viento_fuerza_D2= limpiarLista(tabla_viento_dia2, 2)
    viento_D2= filtrarViento(viento_fuerza_D2)
    fuerza_D2= filtrarFuerza(viento_fuerza_D2)
    dir_Viento_D2= limpiarLista(tabla_direccion_viento_dia2, 2)
    gusts_D2= limpiarLista(tabla_racha_dia2, 1)

    dia3= get_lista(tabla_dia_3)
    temp_D3= limpiarLista(tabla_temp_dia3, 2)
    viento_fuerza_D3= limpiarLista(tabla_viento_dia3, 2)
    viento_D3= filtrarViento(viento_fuerza_D3)
    fuerza_D3= filtrarFuerza(viento_fuerza_D3)
    dir_Viento_D3= limpiarLista(tabla_direccion_viento_dia3, 2)
    gusts_D3= limpiarLista(tabla_racha_dia3, 1)

    
    
    ##################### Creamos objetos con la información diaria ######################

    data1= data(dia1, hora_dia1, temp_D1, viento_D1, fuerza_D1, gusts_D1, dir_Viento_D1)
    data2= data(dia2, hora_dia2, temp_D2, viento_D2, fuerza_D2, gusts_D2, dir_Viento_D2)
    data3= data(dia3, hora_dia3, temp_D3, viento_D3, fuerza_D3, gusts_D3, dir_Viento_D3)

    dataApi=[data1, data2, data3]
    
    ##################### Guardamos la data en un archivo JSON #######################
    with open('apiWind.json', 'w') as apiWind:
        json.dump(dataApi, apiWind)

    driver.quit()
    return dataApi


