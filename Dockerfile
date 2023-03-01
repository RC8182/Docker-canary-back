FROM tiangolo/uvicorn-gunicorn:python3.11-slim

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
WORKDIR /app

# Copiamos librerias python al contenedor
COPY requirements.txt /app/requirements.txt

# Instalamos librerias en el contenedor
RUN python -m pip install --upgrade pip && \
    python -m pip install --no-cache-dir -r /app/requirements.txt
 
# Copiamos el contenido de app en el contenedor
COPY . .

# Damos permisos 
RUN chmod 777 data   

ENV VIENTO_ACTUAL1="https://www.windguru.cz/station/3209"
ENV VIENTO_ACTUAL2="https://cabezo.bergfex.at/"
ENV PRONOSTICO_VIENTO="https://muchoviento.net/El%20M%C3%A9dano%20-%20Playa%20Sur/forecast72"

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


