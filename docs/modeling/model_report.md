# Reporte del Modelo Final.

## Resumen Ejecutivo

El presente apartado presenta el reporte general del modelo de clasificación que ha sido seleccionado, así como los hiperparametros identificados para el modelo de mejor desempeño. En este documento, también se relaciona el respectivo análisis y las conclusiones de la selección del mismo.

## Descripción del Problema.

El presente proyecto tiene como objetivo el entrenar un modelo que permita de manera eficiente la clasificación de pacientes que presenten diagnóstico de diabetes, a partir de una serie de condiciones que se han identificado pudieran ser relevantes al momento de establecer un diagnóstico de diabetes.

Se esperaba que la aplicación de un modelo de clasificación, en este caso **Randon Forest** resultara efectivo en la identificación del diagnóstico, para este ejercicio se obtuvo una exactitud superior el **0.97** en la identificación de los diagnósticos, lo cual resulta ser una métrica bastante adecuada para este tipo de estudios.

La aplicación de técnicas de Aprendizaje de Maquina para clasificación resultan una herramienta relevante en la posible identificación de pacientes que pudieran tener mayor riesgo de presentar diabetes.

## Descripción Del Modelo.

Se utiliza un clasificador de **Arboles Aleatorios** de scikit-learn en donde lo entrenamos el conjunto de datos, en donde se obtiene una exactitud de entrenamiento del 99.91% y su rendimiento en la exactitud en prueba es de 94-85%.

La identificación de hiperparámetros se realizó utilizando **GridsearchCV** para encontrar la combinación optima de hiperparámetros, a continuación se muestran los valores identificados en cada uno de los parámetros.

•	Criterion = Entropy.

•	max_depth=50. 

•	min_samples_leaf=5.

•	min_samples_split=10. 

•	n_estimators=50.

## Evaluación del Modelo.

Al observar las métricas calculadas, se puede decir en general que el modelo de **random forest** presenta un accuracy de **0.97**, lo que significa que un gran número de las clasificaciones eme hace son satisfactorias, tan solo un pequeño porcentaje de ellas se clasifica de manera incorrecta. Con respecto a cada clase podemos ver que 'no diabetes' presenta una precisión de 0.97, recall de 1, y f1-score de 0.98, lo que indica que la mayoría los registros de entrada al modelo que pertenecen a esta clase se identifican de manera correcta.

La clase diabetes por su parte, tiene una precisión de 1, un recall de 0.68, y un F1-score de 0.81, que indica que a pesar de que el modelo distingue bien entre las etiquetas negativas y positivas, tiene problemas en clasificar aquellas que son positivas como positivas; es decir que, existen algunos casos donde se presenta diabetes los define como casos de no diabetes, lo que perjudica a su rendimiento y se ve reflejado en el parámetro Recall y en el F1-Score.

|              | precision | recall | f1-score | support |
|--------------|-----------|--------|----------|---------|
| No_Diabetes  | 0.9701    | 0.9995 | 0.9846   | 17534   |
| Diabetes     | 0.9923    | 0.6810 | 0.8077   | 1696    |
| accuracy     |           |        | 0.9714   | 19230   |
| macro avg    | 0.9812    | 0.8403 | 0.8961   | 19230   |
| weighted avg | 0.9720    | 0.9714 | 0.9690   | 19230   |

## Conclusiones y Recomendaciones

Una vez se realiza la selección del modelo de mejor desempeño, así como la identificación de los mejores de los hiperperametros para el modelo, se concluye que el modelo de clasificación **Randon Forest** es el que presente mejor desempeño pare este proyecto. El valor promedio de la exactitud es superior el 0.97, de igual manera, es un modelo capaz de detectar de manera efectiva los casos en que se registra Diabetes, lo cual se observa en le matriz ce confusión.
Por otra serte, se evidencio que este modelo, cumple a cabalidad el objetivo de la presente investigación ya que, si permite clasificar a partir de una serie de condiciones a pacientes que pudieran tener un diagnóstico de diabetes, también es un modelo versátil y que no requiere de muchos recursos computacionales, lo cual lo hace óptimo para ser empelado por diferentes usuarios como pueden ser doctores o inclusive el usuario final desde un servicio que le permita ingresar los parámetros y saber si es  pudiera presentar un diagnóstico de diabetes.

## Referencias

•	Pedregosa, F., Varoquaux, G., Gramfort, A., Michel V. and Thirion, B., Grisel, O., Blondel, M., Prettenhofer P. and Weiss. R., Dubourg, V., Vanderplas, J., Passos. A., Coumapeau, D., Brucher, M., Perrot, M., & Duchesnay, E. (2011). Scikit-learn: Machine Learning in Python. Journal of Machine Learning Research, 12. 2825-2830.


