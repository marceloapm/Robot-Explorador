# Robot-Explorador

Para Poder hacer uso de el codigo en Python debe subirlo a al directorio principal de la raspberry pi /home/pi

cd /home/pi/

y ejecutar el script en python desde la rasberry con:

sudo nano servidor.py

Luego debe ejecutar el codigo en Processigng, pero antes de darle play asegurece de que tanto la pc desde donde
desea conectarse a la raspberry, como la raspberry estan conectadas a la misma red local LAN

Y en la linea del codigo en processing:

" myClient = new Client(this, "192.168.1.120", 1976);"

Debe cambiar "192.168.1.120" por la direccion IP local que tenga asignada tu raspberry.

Ya quedan conectadas tu raspberry con la pc y podras manejar tu robot explorador con las teclas de direccion del teclado del computador.
