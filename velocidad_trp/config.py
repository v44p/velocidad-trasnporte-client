import os

# api keys
client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')

# storage account
account_key = os.environ.get('STORAGE_ACCOUNT_KEY')
account_name = os.environ.get('STORAGE_ACCOUNT_NAME')
container_name = os.environ.get('CONTAINER_NAME')

# api url
url_file = 'response_api/test_response.txt'
url_transporte = 'https://apitransporte.buenosaires.gob.ar/colectivos/vehiclePositionsSimple'

#vehiclePositionsSimple

# params 
TIEMPO_ESPERA = 30
#RETURN_EXITOSO = 0
#RETURN_FALLIDO = 1
