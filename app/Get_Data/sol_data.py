from astral import LocationInfo
from astral.sun import sun
from datetime import date
import json

def get_sun_state():
    hoy= date.today()
    ciudad = LocationInfo("El Médano", "Spain", "Europe/Canary Island", 28.04510028059856, -16.536500855913307)

    s = sun(ciudad.observer, hoy)
    print((
        f'Dawn:    {s["dawn"]}\n'
        f'Sunrise: {s["sunrise"]}\n'
        f'Noon:    {s["noon"]}\n'
        f'Sunset:  {s["sunset"]}\n'
        f'Dusk:    {s["dusk"]}\n'
    ))

    api_sun= {
            'alba':s["dawn"].time().isoformat(timespec="minutes"),
            'amanecer':s["sunrise"].time().isoformat(timespec="minutes"),
            'mediodia':s["noon"].time().isoformat(timespec="minutes"),
            'atardecer':s["sunset"].time().isoformat(timespec="minutes"),
            'crepusculo':s["dusk"].time().isoformat(timespec="minutes"),
         }
    with open('data/apiSun.json', 'w') as escribir:
        try:
            json.dump(api_sun, escribir)
        except:
            print('No se ha podido escribir')           

    return 

