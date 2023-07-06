from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

async def get_driver(url):    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless") 
    chrome_options.add_argument("--disable-gpu") 
    
    driver =  webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=chrome_options)
    driver.get(url)

    return driver

# Creamos una función para iterar sobre la info pedida y almazenarla en una lista
def get_lista(list):
    lista=[]
    for i in range(len(list)):
        lista.append(list[i].text)  
    return lista

# Creamos una funcion para traducir la fecha en Ingles al Español
def translate_date(str):
    # Nos llega una lista con un str
    # Pasamos el str a obj fecha
    str_a_obj= datetime.strptime(str[0], "%A, %d. %b") 
    obj_fecha= str_a_obj
    # Extraemos el número dia de la semana del objeto fecha y lo pasamos a int
    n_dia_semana= int(datetime.strftime(obj_fecha, "%w"))
    # Extraemos el número dia mes del objeto fecha y lo pasamos a int
    n_dia_mes= int(datetime.strftime(obj_fecha, "%d"))
    # Extraemos el número mes del objeto fecha y lo pasamos a int
    n_mes= int(datetime.strftime(obj_fecha, "%m"))
    # Comenzamos a crear el str a partir de objeto fecha desglosado
    diasSemana=("Sábado", "Domingo", "Lunes", "Martes", "Miércoles", " Jueves", "Viernes")
    nombre_dia_semana= diasSemana[n_dia_semana]
    mesesAnio = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    mes_anio= mesesAnio[n_mes -1]

    return f'{nombre_dia_semana}, {n_dia_mes} de {mes_anio}'