FROM python:3.9.17-slim-bullseye

# Instalamos Chrome y CromeDriver en el contenedor
RUN apt-get update && \
    apt-get install -y gnupg wget curl unzip --no-install-recommends && \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list && \
    apt-get update -y && \
    apt-get install -y google-chrome-stable && \
    CHROMEVER=$(google-chrome --product-version | grep -o "[^\.]*\.[^\.]*\.[^\.]*") && \
    DRIVERVER=$(curl -s "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROMEVER") && \
    wget -q --continue -P /chromedriver "http://chromedriver.storage.googleapis.com/$DRIVERVER/chromedriver_linux64.zip" && \
    unzip /chromedriver/chromedriver* -d /chromedriver

# Seleccionamos directorio de trabajo
WORKDIR /schedule

# Copiamos librerias python al contenedor
COPY requirements.txt /schedule/requirements.txt

# Instalamos librerias en el contenedor
RUN python -m pip install --upgrade pip && \
    python -m pip install --no-cache-dir -r /schedule/requirements.txt
 
# Copiamos el contenido de schedule en el contenedor
COPY . .

# Damos permisos 
RUN chmod 777 data   

ENV VIENTO_ACTUAL1="https://www.windguru.cz/station/3209"
ENV VIENTO_ACTUAL2="https://cabezo.bergfex.at/"
ENV WEATHER_DATA="https://api.open-meteo.com/v1/forecast?latitude=28.05&longitude=-16.54&hourly=temperature_2m,weathercode,windspeed_10m,windgusts_10m,winddirection_10m,uv_index&models=gfs_global&current_weather=true&windspeed_unit=kn&timezone=Europe%2FLondon"
ENV MAREAS_DATA="https://ideihm.covam.es/api-ihm/getmarea?request=gettide&id=64&format=json&month=202307"


EXPOSE 8001

CMD ["python", "main.py"]


