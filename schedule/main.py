# Create Rocketry app
from rocketry import Rocketry
app = Rocketry(execution="async")
import asyncio
import json
from Get_Data.viento_actual_data import get_Data_viento_actual
from Get_Data.weather_data import get_weather
from Get_Data.mareas_data import get_mareas
from Get_Data.sol_data import get_sun_state

# Create some tasks
########## Update BBDD ##############

@app.task('every 180 seconds')
async def updateViento():
    print('Actualizando Viento')
    asyncio.run(await get_Data_viento_actual()  ) 
    return{ print('tasks completed...') }  

@app.task('daily')
async def updateMareas(): 
    print('Llamando a Mareas')
    try:
        await get_mareas()
        print('Task completed!')
    except:
        print('mareas not updated')
    return json.dumps({'msg': 'Task completed!'}) 

@app.task('daily')
async def updateWeather():
    print('Actualizanso weather...')
    try:
        await get_weather()
        print('Task completed!')
    except:
        print('Weather not updated!')
    return json.dumps({'msg': 'Task completed!'})     

@app.task('daily')
async def updateSun():    
    print('Actualizando Estado Sol...')    
    try:
        get_sun_state()
        print('Task completed!')
    except:
        print('Estado Sol not updated!')
    return json.dumps({'msg': 'Task completed!'})   

if __name__ == "__main__":
    app.run()