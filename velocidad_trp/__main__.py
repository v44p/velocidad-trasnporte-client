'''
    Trae la información de posición de la api de transporte de los gps
    y luego la almacena en el storage de transporte. 
'''
import time

from velocidad_trp.objects import VelocidadTransporte, DataStorage
from velocidad_trp.config import *

RETURN_EXITOSO = True


def main():

    print('[INFO] ....')
    print(f'url %s' % url_transporte)
    print(f'cliente %s' % client_id)
    print(f'secrete %s' % client_secret)
    print('...............')

    print('[INFO] ....')
    print(f'container %s' % container_name)
    print(f'account name %s' % account_name)
    print(f'account key %s' % account_key)
    print('...............')

    velocidad = VelocidadTransporte(url_transporte, client_id, client_secret)
    data_storage = DataStorage(container_name, account_name, account_key)
    data_storage.connect_storage()
    while True:
        
        velocidad.get_json

        name_file_local = velocidad.name_file
        (hour, minute, second ) = name_file_local[3:]
        #url_storage = '/'.join([str(s) for s in name_file_local])
        path_local = f'vel_trp_%s_%s_%s.json' % (hour, minute, second)

        try:
            data_storage.upload_blob(
                name_file_local, path_local
                )
            velocidad.delete_json                
            print(f'[INFO] Se guardo: %s' % name_file_local )
        except:
            print('[Error] no se pudo guardar')

        time.sleep(TIEMPO_ESPERA)
    
    return RETURN_EXITOSO


if __name__ == "__main__":
    main()