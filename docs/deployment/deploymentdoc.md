# Despliegue de modelos

## Infraestructura

- **Nombre del modelo:** Se llama diabetes_model y es un modelo de Random Forest. 
- **Plataforma de despliegue:** La plataforma utilizada fue MLflow.
- **Requisitos técnicos:** (lista de requisitos técnicos necesarios para el despliegue, como versión de Python, bibliotecas de terceros, hardware, etc.)
- **Requisitos de seguridad:** El modelo esta pensado para ser desplegado en los hospitales, en donde el hospital brindara los datos, las personas encargadas para ingresar serían los doctores, en donde se tendría un servicio de autenticación, en donde se tendría una lista de usuarios permitidos.
- **Diagrama de arquitectura:** (imagen que muestra la arquitectura del sistema que se utilizará para desplegar el modelo)

## Código de despliegue

- **Archivo principal:** El modelo es desplegado en MLflow, nuestro archivo principal es el nombre del modelo que es diabetes_model.
- **Rutas de acceso a los archivos:** Se encuentra en la rama evaluación_despliegue, en la carpeta script, en la subcarpeta evaluation se encontrara el modelo y el despliegue.
- **Variables de entorno:**
  1) La variable NGROK_TOKEN, seria exponer el servidor MLflow localmente a través de internet, en donde se establece con tu token de ngrok.
  2) La variable MLFLOW_TRACKING_URI, en donde establece el entorno para apuntar al servidor de seguimiento en MLflow, se establece en http://localhost:5000.
  3) La otra variable es el puerto de despliegue, que genera una API que se encuentra en el puerto 8001.

## Documentación del despliegue

- **Instrucciones de instalación:** (instrucciones detalladas para instalar el modelo en la plataforma de despliegue)
- **Instrucciones de configuración:** (instrucciones detalladas para configurar el modelo en la plataforma de despliegue)
- **Instrucciones de uso:** (instrucciones detalladas para utilizar el modelo en la plataforma de despliegue)
- **Instrucciones de mantenimiento:** (instrucciones detalladas para mantener el modelo en la plataforma de despliegue)
