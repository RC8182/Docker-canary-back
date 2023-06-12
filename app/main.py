import uvicorn
from fastapi import FastAPI
import json
import os
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

########## Update BBDD ##############

@app.get('/A28P645I455@api/update-viento')
async def updateViento():
    print('Actualizando Viento')
    get_Data_viento_actual()  
    return{ print('tasks completed...') }  

@app.get('/A28P645I455@api/update-weather')
async def updateWeather():
    print('Actualizanso weather...')
    try:
        get_weather()
        print('Task completed!')
    except:
        print('Weather not updated!')
    return json.dumps({'msg': 'Task completed!'})

@app.get('/A28P645I455@api/update-sun')
async def updateSun():    
    print('Actualizando Estado Sol...')    
    try:
        get_sun_state()
        print('Task completed!')
    except:
        print('Estado Sol not updated!')
    return json.dumps({'msg': 'Task completed!'})     

@app.get('/A28P645I455@api/update-mareas')
async def updateMareas(): 
    print('Llamando a Mareas')
    try:
        get_mareas()
        print('Task completed!')
    except:
        print('mareas not updated')
    return json.dumps({'msg': 'Task completed!'})

############### Response ==> Viento Weather Sun ############

@app.get('/A28P645I455@api')
async def apiMeteo():

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

######### Response ==> Mareas ############

@app.get('/A28P645I455@api/mareas')
async def apiMareas():
    with open('data/apiMareas.json', 'r') as infile:
        try:
            apiMareas= json.load(infile) 
        except:    
            print('Error archivo no encontrado....')
   
    return apiMareas




if __name__=='__main__':
    uvicorn.run('main:app', port= int(PORT), reload= True)

