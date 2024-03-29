from astral import LocationInfo
from astral.sun import sun
from datetime import date, timedelta, datetime
import json

def get_sun_state():
    updated= str(datetime.now())
    dia0= date.today()
    dia1= date.today() + timedelta(1)
    dia2= date.today() + timedelta(2)
    dias=[dia0, dia1, dia2]

    ciudad = LocationInfo("El Médano", "Spain", "Europe/Canary Island", 28.04510028059856, -16.536500855913307)
    listaFechas=[]
    listaStatus=[]
    print(updated)
    for i in dias:
        s = sun(ciudad.observer, i)
        fecha=str(i)
        estado= {
                'alba':s["dawn"].time().isoformat(timespec="minutes"),
                'amanecer':s["sunrise"].time().isoformat(timespec="minutes"),
                'mediodia':s["noon"].time().isoformat(timespec="minutes"),
                'atardecer':s["sunset"].time().isoformat(timespec="minutes"),
                'crepusculo':s["dusk"].time().isoformat(timespec="minutes"),
                }
        listaFechas.append(fecha)
        listaStatus.append(estado)

    api_sun={
        'last_update': updated,
        'fecha': listaFechas,
        'status': listaStatus,
    }   

        
    with open('data/apiSun.json', 'w') as file:
        print('Escribiendo apiSun...')
        try:
            json.dump(api_sun, file)
        except:
            print('No se ha podido escribir')           

    return 

