'''
    Trae la información de posición de la api de transporte de los gps
    y luego la almacena en el storage de transporte. 
'''
import time

from velocidad_trp.objects import VelocidadTransporte
from velocidad_trp.config import *

RETURN_EXITOSO = True

def main():
    velocidad_transporte = VelocidadTransporte(url_transporte, client_id, client_secret)
    while True:
        velocidad_response = velocidad_transporte.get_json
        velocidad = velocidad_response.json()
        print(velocidad)
        time.sleep(TIEMPO_ESPERA)
    return RETURN_EXITOSO


if __name__ == "__main__":
    main()