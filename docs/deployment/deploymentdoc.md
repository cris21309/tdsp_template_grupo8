# Despliegue de modelos

## Infraestructura

- **Nombre del modelo:** Se llama diabetes_model y es un modelo de Random Forest. 
- **Plataforma de despliegue:** La plataforma utilizada fue MLflow.
- **Requisitos técnicos:** (lista de requisitos técnicos necesarios para el despliegue, como versión de Python, bibliotecas de terceros, hardware, etc.)
- **Requisitos de seguridad:** El modelo esta pensado para ser desplegado en los hospitales, en donde el hospital brindara los datos, las personas encargadas para ingresar serían los doctores, en donde se tendría un servicio de autenticación, en donde se tendría una lista de usuarios permitidos.
- **Diagrama de arquitectura:** ![](https://github.com/cris21309/tdsp_template_grupo8/blob/master/docs/deployment/Captura.PNG)

## Código de despliegue

- **Archivo principal:** El modelo es desplegado en MLflow, nuestro archivo principal es el nombre del modelo que es diabetes_model.
- **Rutas de acceso a los archivos:** Se encuentra en la rama evaluación_despliegue, en la carpeta script, en la subcarpeta evaluation se encontrara el modelo y el despliegue.
- **Variables de entorno:**
  1) La variable NGROK_TOKEN, seria exponer el servidor MLflow localmente a través de internet, en donde se establece con tu token de ngrok.
  2) La variable MLFLOW_TRACKING_URI, en donde establece el entorno para apuntar al servidor de seguimiento en MLflow, se establece en http://localhost:5000.
  3) La otra variable es el puerto de despliegue, que genera una API que se encuentra en el puerto 8001.

## Documentación del despliegue

- **Instrucciones de instalación:** Se realiza mediante models serve, que es donde se encuentra el modelo de producción. 
- **Instrucciones de configuración:** (instrucciones detalladas para configurar el modelo en la plataforma de despliegue)
- **Instrucciones de uso:** El doctor tendrá que digitar los datos del paciente que serían de manera ordenada, el género, la edad, si tiene hipertensión, si tiene una enfermedad cardiaca, su historial de tabaco, el índice de masa corporal, su nivel promedio de azúcar en sangre y el nivel de glucosa, le va a retornar un valor entero si es de la clase 0 (no tiene diabetes), o de la clase 1 (tiene diabetes).
- **Instrucciones de mantenimiento:** Si encontramos un nuevo modelo en producción, bajaríamos el servicio y se crea un nuevo servicio con el nuevo modelo.
