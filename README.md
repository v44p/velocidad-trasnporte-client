## Velocidad-client

Cliente para traer los datos de transporte.

## Deploy 

se debería buildear la imagen de docker y luego correr mediante 

´´´
docker run -it -d --rm \
    -e CLIENT_ID=<cliente id> \
    -e CLIENT_SECRET=<client secret> \
    -e STORAGE_ACCOUNT_NAME=<nombre storage> \
    -e STORAGE_ACCOUNT_KEY= <key account> \
    -e CONTAINER_NAME=<container name> \
    -p 8888:8888 \
    --name velocidad-client \
    velocidad-client

´´´


