import os
import json

from velocidad_trp.utils import http_transporte
from datetime import datetime


class VelocidadTransporte:

    url = ''
    client_id = ''
    respuesta = ''
    client_secret = ''
    name_file = ''
    path_local = ''


    def __init__(self, url_transporte:str, client_id:str, client_secret:str ):
        self.url = url_transporte
        self.client_id = client_id
        self.client_secret = client_secret
        

    @property
    def get_json(self):
        params = {
            'client_id':self.client_id,
            'client_secret':self.client_secret
        }
        try:
            print(params)
            r = http_transporte(self.url, params)
            print(r)
            self.respuesta = r.json()
            self.__get_name()
            self.__write_json()
            return True
        except:
            print('Error en Velocidad Transporte')
            return False


    def __get_name(self):
        '''
            Genera un nombre para el archivo en base a la fecha.
            Este nombre será usado para guardar en el storage        
        '''
        date_request = datetime.now()
        year = date_request.year
        month = date_request.month
        day = date_request.day
        hour = date_request.hour
        minute = date_request.minute
        second = date_request.second
        self.name_file = [year, month, day, hour, minute, second]
        return True


    def __write_json(self):
        (hour, minute, second ) = self.name_file[3:]
        self.path_local = f'vel_trp_%s_%s_%s.json' % (hour, minute, second)
        try:
            with open(self.path_local, 'w') as f:
                json.dump(self.respuesta, f)
        except:
            print('no se pudo guardar')

    @property   
    def delete_json(self):
        '''
            Elimina el json en la vm
        '''
        try:
            os.remove(self.path_local)
            print(f'[INFO] delete s%' % self.path_local)
        except:
            print('No exise')




class Storage:

    response = ''
    url_file = ''
    container_name = ''

    def __init__(self, container_name, account_name, account_key):
        self.container_name = container_name
        self.account_name = account_name
        self.account_key = account_key


    def connect_storage(self):
        pass


        

class DataStorage(Storage):
    '''
        Esta clase toma la libreria para conectarse a un blob storage,
        de la misma forma podría crearse una clase para otro tipo de 
        almacenamiento.
    '''
    
    block_blob_service = ''
    container_name = ''

    
    def connect_storage(self):
        from azure.storage.blob import BlockBlobService, PublicAccess
        print(self.account_name)
        print(self.account_key)
        try:
            self.block_blob_service = BlockBlobService(
                account_name=self.account_name,
                account_key=self.account_key
                )
            #return block_blob_service
        except:
            print('ERROR' + ' No se pudo conectar')
            #return False


    def upload_blob(self, prefix_container, name_file):
        path_full_container = 'input_api/'\
                + '/'.join([str(s) for s in prefix_container[:3]])\
                + '/' + name_file

        print('[INFO] Subiendo archivo a container ...')
        print('[INFO]', self.container_name)
        print('[INFO]', path_full_container)
        print('[INFO]', name_file) 
        print()               
        #try:
        self.block_blob_service\
            .create_blob_from_path(
                self.container_name,
                path_full_container,
                name_file
            )
        #except:
        #    print('No se pudo copiar al storage')




class DataLake(Storage):
    pass


if __name__ == '__main__':
    pass