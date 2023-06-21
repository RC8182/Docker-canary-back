FROM python:3.9.17-slim-bullseye


# Seleccionamos directorio de trabajo
WORKDIR /api

# Copiamos librerias python al contenedor
COPY requirement.txt /api/requirement.txt

# Instalamos librerias en el contenedor
RUN python -m pip install --upgrade pip && \
    python -m pip install --no-cache-dir -r /api/requirement.txt
 
# Copiamos el contenido de app en el contenedor
COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

