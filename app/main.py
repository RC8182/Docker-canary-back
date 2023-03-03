import uvicorn
from fastapi import FastAPI
import json
import time
from fastapi_utils.tasks import repeat_every
from Get_Data.viento_actual_data import *
from Get_Data.pronostico_data import *
from Get_Data.mareas_data import *
from Get_Data.sol_data import *




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
@repeat_every(seconds=60 * 6)  
def updateVientoActual():
    scrap_Data_viento_actual()

@app.on_event("startup")
@repeat_every(seconds=60*60)
def updateViento():
    scrap_pronostico_viento()
    get_sun_state()
    get_mareas() 
 

time.sleep(5)

@app.get('/')
def apiVientos():

    with open('data/apiActualWind.json', 'r') as infile:
        try:
            apiVientoActual= json.load(infile)
        except:
            print('Error archivo no encontrado....')
             

    with open('data/apiWind.json', 'r') as infile:
        try:
            apiViento= json.load(infile) 
        except:    
            print('Error archivo no encontrado....')

    with open('data/apiSun.json', 'r') as infile:
        try:
            apiSol= json.load(infile) 
        except:    
            print('Error archivo no encontrado....')

    return [ apiVientoActual, apiViento, apiSol]

@app.get('/mareas')
def apiMareas():
    with open('data/apiMareas.json', 'r') as infile:
        try:
            apiMareas= json.load(infile) 
        except:    
            print('Error archivo no encontrado....')
    return apiMareas

if __name__=='__main__':
    uvicorn.run('main:app', port=8000, reload= True)

