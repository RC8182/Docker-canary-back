import uvicorn
from fastapi import FastAPI
import json


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



############### Response ==> Viento Weather Sun ############

@app.get('/A28P645I455@api')
async def apiMeteo():

    with open('schedule/data/apiActualWind.json', 'r') as infile:
        try:
            apiVientoActual= json.load(infile)
        except:
            print('Error archivo no encontrado....')
             

    with open('schedule/data/apiWeather.json', 'r') as infile:
        try:
            apiWeather= json.load(infile) 
        except:    
            print('Error archivo no encontrado....')

    with open('schedule/data/apiSun.json', 'r') as infile:
        try:
            apiSol= json.load(infile) 
        except:    
            print('Error archivo no encontrado....')
         

    return [apiVientoActual, apiWeather, apiSol]

######### Response ==> Mareas ############

@app.get('/A28P645I455@api/mareas')
async def apiMareas():
    with open('schedule/data/apiMareas.json', 'r') as infile:
        try:
            apiMareas= json.load(infile) 
        except:    
            print('Error archivo no encontrado....')
   
    return apiMareas




if __name__=='__main__':
    uvicorn.run('main:app', port= int(8000), reload= True)

