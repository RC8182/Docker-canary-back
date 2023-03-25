import uvicorn
from fastapi import FastAPI
import json
import time
import os
from fastapi_utils.tasks import repeat_every
from Get_Data.viento_actual_data import get_Data_viento_actual
from Get_Data.weather_data import get_weather
from Get_Data.mareas_data import get_mareas
from Get_Data.sol_data import get_sun_state
PORT= os.getenv('PUERTO')



app= FastAPI()
#----------------------- Midleware -----------------------#
from fastapi.middleware.cors import CORSMiddleware
origins = [

    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
@repeat_every(seconds=60 * 10)  
def updateVientoActual():
    print(time.localtime())
    get_Data_viento_actual()
    get_weather()
    

@app.on_event("startup")
@repeat_every(seconds=60*60)
def updateViento():
    print(time.localtime())
    get_sun_state()
    get_mareas() 
 

time.sleep(5)

@app.get('/A28P645I455@api')
def apiMeteo():

    with open('data/apiActualWind.json', 'r') as infile:
        try:
            apiVientoActual= json.load(infile)
        except:
            print('Error archivo no encontrado....')
             

    with open('data/apiWeather.json', 'r') as infile:
        try:
            apiWeather= json.load(infile) 
        except:    
            print('Error archivo no encontrado....')

    with open('data/apiSun.json', 'r') as infile:
        try:
            apiSol= json.load(infile) 
        except:    
            print('Error archivo no encontrado....')
         

    return [apiVientoActual, apiWeather, apiSol]

@app.get('/A28P645I455@api/mareas')
def apiMareas():
    with open('data/apiMareas.json', 'r') as infile:
        try:
            apiMareas= json.load(infile) 
        except:    
            print('Error archivo no encontrado....')
   
    return apiMareas


if __name__=='__main__':
    uvicorn.run('main:app', port= int(PORT), reload= True)

