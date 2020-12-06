import os
import json
import requests

from velocidad_trp.utils import http_transporte
from datetime import datetime


class VelocidadTransporte:

    url = ''
    client_id = ''
    respuesta = ''
    client_secret = ''
    name_file = ''
    path_local = ''
    params = {
        'client_id':"",
        'client_secret':""
    }

    def __init__(self, url_transporte:str, client_id:str, client_secret:str ):
        self.url = url_transporte
        self.params["client_id"] = client_id
        self.params["client_secret"] = client_secret

    @property
    def get_json(self):
        try:
            r = requests.get(self.url, params=self.params, timeout=10)
            if r.status_code != 200:
                print(f'Error request %d' % (r.status_code))
                return None
            return r
        except:
            print('Error en Velocidad Transporte')
            return None

    def __write_json(self):
        pass



if __name__ == '__main__':
    pass