FROM python:3.10

WORKDIR /app

# copia el archivo de dependencias al contenedor
COPY requirements.txt /app/requirements.txt

# instalacion de las dependencias necesarias
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8000

RUN ls -la /app

# ejecuta los comando en servidor python
CMD [ "python", "mange.py", "runserver", "0.0.0.0:8000"]