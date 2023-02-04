import uvicorn
from fastapi import FastAPI
import json
from fastapi_utils.tasks import repeat_every
from Get_Data.windguru_data import *
from Get_Data.muchoviento_data import *



app= FastAPI()
#----------------------- Midleware -----------------------#
from fastapi.middleware.cors import CORSMiddleware
origins = [

    "*"
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
    scrap_Data_windguru()

@app.on_event("startup")
@repeat_every(seconds=60*60)
def updateViento():
    scrap_MuchoViento()


@app.get('/')
def api():
    with open('./apiActualWind.json', 'r') as infile:
        apiVientoActual= json.load(infile)
    with open('apiWind.json', 'r') as infile:
        apiViento= json.load(infile) 
    
    return [apiVientoActual, apiViento]

if __name__=='__main__':
    uvicorn.run('main:app', port=8000, reload= True)

