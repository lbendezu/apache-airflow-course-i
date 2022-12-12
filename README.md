# apache-airflow-course-i
Repositorio del curso de Apache Airflow

## Pasos la preparación inicial

1. Crear una carpeta "airflow" en donde tendremos todo lo necesario para ejecutar Airflow en nuestro entorno local
2. Descargar el archivo .env que se encuentra en la raíz "Clase02" del código fuente
3. Descargar el archivo [docker-compose](https:/airflow.apache.org/docs/apache-airflow/2.4.2/docker-compose.yaml) 
4. Ejecutar el comando (con esto se generarán las carpetas dags, logs y plugins)
```
docker compose up airflow-init
```
5. Limpiar contenedores utilizando
```
docker-compose down
```

## Pasos para ejecutar airflow

1. Ejecutar el comando
```
docker-compose up --build
```
2. Cuando termine de cargar el paso 1, en un navegador ir a la dirección http://localhost:8080


## Pruebas del API Estable de Airflow con Postman:

Utilizar el archivo "DataScienceResearchPeru.postman_collection.json" que se encuentra en la raíz del repositorio para importar la colección en Postman y porder revisar las peticiones revisadas en clase.