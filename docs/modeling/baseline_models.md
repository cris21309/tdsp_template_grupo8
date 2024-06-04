# Reporte del Modelo Baseline

Este documento contiene los resultados de los diferentes modelos Baseline, el análisis fue apoyado empleando la herramienta MLflow, tomando como métrica clave el Acurracy o la exactitud de los modelos.

## Descripción del modelo

Los modelos que utilizamos son:
**Regresión Logística** Es una técnica de análisis de datos que utiliza las matemáticas para encontrar las relaciones entre dos factores de datos. Luego, utiliza esta relación para predecir el valor de uno de esos factores basándose en el otro, es uno de los algoritmos más empleados debido a su eficiencia y robustez para clasificación binaria, además de su eficiencia computacional.

**Maquina de soporte Vectorial** Otro algoritmo utilizado es el suport vector machine para clasificación, que se caracteriza por buscar una región optima que separe diferentes clases de datos en un margen considerable. Es decir que buscar un hiper plano que maximice la distancia entre las clases que se necesite diferenciar, además que puede trabajar en casos de linealidad y no linealidad.

**K Vecinos cercanos** Algoritmo de k vecinos más cercanos, también conocido como KNN o k-NN, es un clasificador de aprendizaje supervisado no paramétrico, que utiliza la proximidad para hacer clasificaciones o predicciones sobre la agrupación de un punto de datos individual.

**Gradiente Descendiente Estocástico** El descenso del gradiente es un algoritmo de optimización que se utiliza comúnmente para entrenar modelos de aprendizaje automático y redes neuronales. Entrena modelos de aprendizaje automático minimizando los errores entre los resultados previstos y los reales, presenta un buen desempeño en ejercicio de clasificación binaria.

**Los árboles de decisión** Este es un algoritmo de aprendizaje supervisado utilizado para problemas de clasificación. Funciona construyendo un árbol de decisiones en el que cada nodo representa una característica, cada borde representa una regla de decisión y cada hoja representa la etiqueta de clase.

**Bosques Aleatorios** Bosque aleatorio es un método de aprendizaje que opera mediante la construcción de múltiples árboles de decisión. La decisión final se toma en base a la mayoría de los árboles, es un algoritmo muy potente que se ajusta muy bien a problemas de clasificación.

## Variables de entrada

Las variables de entrada son:
•	Genero del paciente del reporte.
•	Edad del entrevistado.
•	Presente hipertensión.
•	Tiene una enfermedad cardiaca. 
•	Historial de tabaco.
•	índice de Masa Corporal. 
•	Nivel promedio de azúcar en sangre.
•	Nivel de glucosa.


## Variable objetivo
La variable objetivo es la columna diabetes en donde nos indica si esta persona tiene esa enfermedad siendo esta una variable booleana identificando la presencia o no del diagnóstico.

## Evaluación del modelo

### Métricas de evaluación

Para la evaluación del desempeño de los modelos de clasificación se emplearon las siguientes métricas:

•	**Acurracy o exactitud**: esta fue la principal métrica empleada y la que se contempló en la comparación en MLflow, se define como mide la frecuencia con la que el clasificador predice correctamente. Podemos definir la precisión como la relación entre el número de predicciones correctas y el número total de predicciones.

•	**Precisión**: Explica cuántos de los casos pronosticados correctamente resultaron ser positivos. La precisión es útil en los casos en los que los falsos positivos son una preocupación mayor que los falsos negativos.

•	**Recall o sencibilidad**:  Explica cuántos de los casos positivos reales puede predecir correctamente el modelo. La recuperación es una métrica útil en los casos en los que el falso negativo es más preocupante que el falso positivo

•	**F1-score**: Da una idea combinada sobre las métricas de precisión y recuperación. Siendo la media Armónica de las medidas.

•	**Resultado de Matriz de confusión**: para un mayor entendimiento se tuvo en cuenta la matriz de confusión.

### Resultados de evaluación

Tabla que muestra los resultados de evaluación del modelo baseline, incluyendo las métricas de evaluación.

## Análisis de los resultados

Una vez adelantado el análisis de los resultados evidenciamos que el desempeño en cuanto a la clasificación de los diferentes modelos resulta ser satisfactorio, todos los métodos presentaron valores de Acurracy superior al 94% para la clasificación de valores.
Así bien. el modelo por regresión logística tuvo un acurracy de 0.9596 acertando en 18.453 ocasiones (No diabetes 17.376 y Diabetes 1077), por otra parte, en el caso de SVM se registró una exactitud de 0.9593 con un total de 18449 (No diabetes 17.466 y Diabetes 983), mientras que para el caso de KNN se cuenta con un desempeño de 0.9592n con un registro de aciertos de 18483 (No diabetes 17.452 y Diabetes 1031), para el caso de SGD el valor del acurracy es de 0.9575 para un total de 18483 (No diabetes 17.452 y Diabetes 1031), finalmente, para el caso de modelo por arboles aleatorios se registró una exactitud de 0.9705. acertando en 18684 (No diabetes 17.534 y Diabetes 1150).

En general como muestran los reportes se evidencia un buen desempeño en clasificación, en cada uno de los modelos siendo relevante la correcta identificación de los valores positivos.

## Conclusiones

Una vez se realiza el análisis de los resultados de los diferentes modelos, se observa que el modelo por **Bosques aleatorios - Random forest** tiene un leve desempeño mejor siendo el único cuyo valor de exactitud es superior a 0.96, de igual manera, es el que mayor cantidad de aciertos presenta y el que representa de manera más satisfactoria los casos positivos (cuando tienen diabetes dentro de la matriz de confusión), siendo esto una de las métricas de evaluación del proyecto más importantes del estudio.

## Referencias

•	Pedregosa, F., Varoquaux, G., Gramfort, A., Michel V. and Thirion, B., Grisel, O., Blondel, M., Prettenhofer P. and Weiss. R., Dubourg, V., Vanderplas, J., Passos. A., Coumapeau, D., Brucher, M., Perrot, M., & Duchesnay, E. (2011). Scikit-learn: Machine Learning in Python. Journal of Machine Learning Research, 12. 2825-2830.

