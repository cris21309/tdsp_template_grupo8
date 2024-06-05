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

| Modelo | Accuracy | Precision | Recall | F1-score |
| --- | --- | --- | --- | ---  |
| Regresión Logística | 0.96 | 0.87 | 0.63 | 0.73 |
| C-Support Vector Classification | 0.96 | 0.94 | 0.57 | 0.72 |
| K-Nearest Neighbors Classifier | 0.96 | 0.93 | 0.61 | 0.73 |
| Stochastic Gradient Descent Classifier  | 0.96 | 0.84 | 0.64 | 0.73 |
| Árbol de decisión | 0.97 | 1.0 | 0.67 | 0.80 |
| Bosques aleatorios | 0.97 | 0.99 | 0.68 | 0.81 |

### Descripción de los resultados y su relevancia para el negocio

-	El modelo de Random Forest utilizando GridsearchCv alcanzo una precisión superior al 97%, lo que sugiere un rendimiento sólido en la identificación de casos de diabetes. Se observa una alta precisión en la identificación de pacientes sin diabetes, con una precisión, recall y F1-Scores cercanos a 1, sin embargo, hubo desafíos en la identificación de casos positivos de diabetes, lo que se reflejo en un recall y F1-score mas bajos para la clase.
  
-	El modelo tiene una relevancia significativa para el negocio, ya que pueden mejor la eficiencia clínica, reducir costos, informar políticas de salud pública y promover el autocuidado, lo que en ultima instancia conduce a una mejora en los resultados de la salud del paciente. 


## Lecciones aprendidas

### Desafíos y obstáculos encontrados durante el proyecto

-	Uno de los principales desafíos fue mejorar el modelo ya que la mayoría de los modelos se obtenía una precisión alta y que a la vez no se sobreajustara el modelo y otro de los retos fue el despliegue en la plataforma MLflow.
  
### Lecciones aprendidas en relación al manejo de los datos, el modelamiento y la implementación del modelo.

-	Al realizarse un buen análisis exploratorio y un debido preprocesamiento, puede mejorar el rendimiento del modelo y facilitar su interpretación.

- Es importante explorar una variedad de algoritmos de aprendizaje automático y evaluar su rendimiento en función de métricas especificas antes de seleccionar el modelo final.

### Recomendaciones

- Utilizar la metodología CRISP-DM u otras metodologías para proyectos de machine learning.
-	Asegurar de recopilar datos de alta calidad y suficiente cantidad para entrenar y validar el modelo. 
-	Mantener los modelos actualizados y adaptar sus estrategias a medida que se recopilen nuevos datos.


## Impacto del proyecto

- El modelo de clasificación de diabetes no solo tiene el potencial de mejorar la atención médica al identificar casos tempranos de la enfermedad, sino que también puede contribuir a la eficiencia operativa y la calidad de vida de los pacientes al empoderarlos para tomar decisiones informadas sobre su salud. 

## Conclusiones

-	Cuando los datos están limpios, completos y bien estructurados y se han realizado análisis exploratorios para comprender la distribución y las características de los datos, los modelos tienen una base sólida para aprender patrones significativos y hacer predicciones precisas.
-	El modelo de Random Forest fue el más adecuado para este proyecto, con una precisión promedio superior al 97%, fue capaz de identificar eficazmente los casos de diabetes, lo que lo hace útil para su implementación en aplicaciones médicas. Además, el modelo es versátil y no requiere muchos recursos computacionales, lo que lo hace óptimo para su uso por parte de diversos usuarios, como médicos o incluso el público en general a través de servicios en línea.
-	Los modelos tradicionales, como los árboles de decisión y bosques aleatorios, pueden ofrecer resultados sobresalientes en una variedad en problemas de aprendizaje automático. Estos modelos pueden ser suficientes para resolver tareas complejas sin la necesidad de utilizar modelos mas avanzados o profundos, como las redes neuronales. 
-	El modelo desarrollado no solo tiene aplicaciones clínicas importantes para la detección y el cuidado de individuos con diabetes, sino que también puede tener un impacto significativo en la salud pública al permitir una intervención temprana y personalizada en la gestión de esta enfermedad crónica.


