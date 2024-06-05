# Informe de salida

## Resumen Ejecutivo

Este informe describe los resultados del proyecto de machine learning y presenta los principales logros y lecciones aprendidas durante el proceso.

## Resultados del proyecto

### Resumen de los entregables 
-	En la primera entrega indicamos una descripción y objetivos del proyecto, en donde es un proyecto que se centra en aplicar técnicas de aprendizaje de maquina en el análisis de la diabetes, nuestros logros son comprender la problemática relacionada con la diabetes y adquirir los datos necesarios para el estudio.
-	En la segunda entrega, realizamos el análisis exploratorio de los datos y el debido preprocesamiento, en nuestra primera parte se identificó una base de datos que contiene 100,000 registros, con 9 columnas, en donde no se encontraron valores nulos y valores atípicos en las variables, ya en la segunda parte se realiza una identificación y eliminación de registros duplicados, la separación de características y etiquetas, el debido preprocesamientos para las diferentes tipos de variables: booleanas, numéricas y categóricas y nuestra parte final es la división del conjunto de datos que fue de 80% para entrenamiento y un 20% para pruebas, el logro de esta parte es asegurar la integridad y calidad de los datos  y prepararlos adecuadamente para la construcción y evaluación de modelos de predicción de la diabetes.
-	en la tercera entrega es el entrenamiento y evalucación de los diferentes modelos empleados en el proyecto, este logro se proporciona una comprensión clara del rendimiento de los diferentes modelos de predicción, identificando que el modelo más prometedor para este propósito es bosques aleatorios.
-	En la cuarta entrega es el despliegue del modelo para el usuario final, en donde el mejor modelo lo seleccionamos para la etapa de producción con la plataforma MLflow, en donde el doctor ingresará los datos del paciente y en donde le dará el resultado de si la persona tiene diabetes o no. En esta parte el logro es conectar el modelo a la plataforma para que el cliente final tenga esa amigabilidad con el sistema en donde solo tenga que digitar los datos y obtener los resultados.

### Evaluación de los modelos

Se realizo el entrenamiento en cinco modelos, regresión logística, máquina de soporte vectorial, K vecinos cercanos, gradiente descendente estocástico y bosques aleatorios, para examinar el modelo lo realizamos con las métricas de exactitud, precisión, sensibilidad y F1-score, todos los modelos tienen un rendimiento bastante alto, con puntajes de precisión, recall y F1-score de alrededor de 0.95 o superior, en donde se determinó que el modelo de bosques aleatorios destaco con una exactitud superior al 97%.

| Modelo | Precision | Recall | F1-score | Accuracy |
| --- | --- | --- | --- | ---  |
| Regresión Logística | 0.96 | 0.96 | 0.96 | 0.96 |
| C-Support Vector Classification | 0.96 | 0.96 | 0.95 | 0.96 |
| K-Nearest Neighbors Classifier | 0.96 | 0.96 | 0.96 | 0.96 |
| Stochastic Gradient Descent Classifier  | 0.95 | 0.96 | 0.95 | 0.96 |
| Árbol de decisión | 0.97 | 0.97 | 0.97 | 0.97 |

### Descripción de los resultados y su relevancia para el negocio

-	El modelo de Random Forest utilizando GridsearchCv alcanzo una precisión superior al 97%, lo que sugiere un rendimiento sólido en la identificación de casos de diabetes. Se observa una alta precisión en la identificación de pacientes sin diabetes, con una precisión, recall y F1-Scores cercanos a 1, sin embargo, hubo desafíos en la identificación de casos positivos de diabetes, lo que se reflejo en un recall y F1-score mas bajos para la clase.
  
-	El modelo tiene una relevancia significativa para el negocio, ya que pueden mejor la eficiencia clínica, reducir costos, informar políticas de salud pública y promover el autocuidado, lo que en ultima instancia conduce a una mejora en los resultados de la salud del paciente. 


## Lecciones aprendidas

- Identificación de los principales desafíos y obstáculos encontrados durante el proyecto.
- Lecciones aprendidas en relación al manejo de los datos, el modelamiento y la implementación del modelo.
- Recomendaciones para futuros proyectos de machine learning.

## Impacto del proyecto

- Descripción del impacto del modelo en el negocio o en la industria.
- Identificación de las áreas de mejora y oportunidades de desarrollo futuras.

## Conclusiones

- Resumen de los resultados y principales logros del proyecto.
- Conclusiones finales y recomendaciones para futuros proyectos.

## Agradecimientos

- Agradecimientos al equipo de trabajo y a los colaboradores que hicieron posible este proyecto.
- Agradecimientos especiales a los patrocinadores y financiadores del proyecto.
