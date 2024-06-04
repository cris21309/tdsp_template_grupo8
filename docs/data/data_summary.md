## **Reporte de Datos**
---
Con la finalidad de tener un mayor entendimiento del proyecto y poder dimensionar en mejor manera el alcance y lo que se pretende en el proyecto, lo primero que se adelantara es el análisis exploratorio del conjunto de datos y de los archivos que hacen parte del dataset.


Normalmente en el análisis exploratorio, se trata de dar respuesta a los siguientes elementos:

## Resumen general de los datos

-------------
En esta sección se presenta un resumen general de los datos. Se describe el número total de observaciones, variables, el tipo de variables, la presencia de valores faltantes y la distribución de las variables, tembien se pretenden responder cuestiones como:

---
- ¿Cuántos Elementos tiene la base de datos?
- ¿Qué tamaño en MB de la base de datos?
- ¿cuales son las variables del análisis?
---------

El Dataset contiene 100000 Registros para estudio de Diabetes

Numero de filas: 100000, Numero de columnas: 9, numero de celdas 900000

| Column      | Non-Null Count | Dtype |
| ----------- | ----------- |--------------|
| gender      | 100000 non-null       | object       |
| age   | 100000 non-null        | float64       |
| hypertension   | 100000 non-null        | int64       |
| heart_disease   | 100000 non-null        | int64       |
| smoking_history   | 100000 non-null        | object       |
| bmi   | 100000 non-null        | float64       |
| HbA1c_level   | 100000 non-null        | float64       |
| blood_glucose_level   | 100000 non-null        | int64       |
| diabetes   | 100000 non-null        | int64       |

**memory usage: 17.3 MB**

## Resumen de calidad de los datos

---
En esta sección se presenta un resumen de la calidad de los datos. Se describe la cantidad y porcentaje de valores faltantes, valores extremos, errores y duplicados. También se muestran las acciones tomadas para abordar estos problema

------

- ¿Hay datos faltantes, celdas vacías o de mala calidad?
- ¿existen valores atipicos o o sin formato?

**Valores Nulos**
| Column      | Nulos |
| ----------- | ----------- |
| gender      | 0|
| hypertension      | 0|
| heart_disease      | 0|
| smoking_history      | 0|
| bmi      | 0|
| HbA1c_level      | 0|
| blood_glucose_level      | 0|
| diabetes      | 0|

----

En la base de datos existen variables de carácter cualitativo como es el género y el historial de fumador, también variables numéricas como es el caso de la edad, el índice de masa corporal (bmi), la prueba de hemoglobina (HbA1c_level) y el nivel de glucosa en sangre, también variables de carácter booleano, como lo son la presencia de hipertensión o de laguna cardiopatía.
Estas consideraciones se deberán tener en cuenta al momento del pre procesamiento con la finalidad de garantizar que el estudio se delante de manera efectiva.

-----

## **Annálisis de Varibles**
-----------
En el siguiente apartado se realiza una exploración general de las diferentes variables que componen la base de datos.

-------------

## Variable objetivo
----------
En esta sección se describe la variable objetivo. Se muestra la distribución de la variable y se presentan gráficos que permiten entender mejor su comportamiento.

-----------
**Análisi de variable Objetivo**
![image](https://github.com/cris21309/tdsp_template_grupo8/assets/162080075/118a54f6-9f83-43de-b0db-fb7afdb395cf)

**Análisis de variables explicativas**
![image](https://github.com/cris21309/tdsp_template_grupo8/assets/162080075/0ee313b3-0008-4f2a-abd8-8ffab5c4426a)

En este apartado se ve el comportamiento de las variables respecto a la variable objetivo, con tal fin se hace uso de un diagrama de conteo para las variables cualitativas y un gráfico de dispersión para las variables numéricas.

En esta se evidencia que, la mayoría de los datos corresponde a no presencia de diabetes, y dentro de estos conjuntos la mayoría de los datos corresponde con mujeres. En cuanto a la relación con el cigarrillo, se observa que para la mayoría de los registros se relaciona o que no fuma o que no se cuenta con información; sin embargo para el caso de los registros con presencia de diabetes no se evidencia una diferencia tan grande para las diferentes categorías.

Al revisar los gráficos de dispersión, no se evidencian relación directa en todos los casos, sin embargo, para los casos de HbA1c_level y nivel de glucosa en sangre, altos valores parecen tener una relación directa con la presencia de diabetes.


## Variables individuales
-----------
En esta sección se presenta un análisis detallado de cada variable individual. Se muestran estadísticas descriptivas, gráficos de distribución y de relación con la variable objetivo (si aplica). Además, se describen posibles transformaciones que se pueden aplicar a la variable.

-----
A continuación se presentan los principales indicadores de dispersión y tendencia central de las variables de tipo numéricas del proyecto.

|   parametro    | age   | hypertension         | heart_disease | bmi      | HbA1c_level         | blood_glucose_level | diabetes   |
|-------|--------------|---------------|------------|-------------|---------------------|------------|------------|
| count | 100000.000   | 100000.000    | 100000.000 | 100000.000  | 100000.000          | 100000.000 | 100000.000 |
| mean  | 41.886       | 0.075         | 0.039      | 27.321      | 5.528               | 138.058    | 0.085      |
| std   | 22.517       | 0.263         | 0.195      | 6.637       | 1.071               | 40.708     | 0.279      |
| min   | 0.080        | 0.000         | 0.000      | 10.010      | 3.500               | 80.000     | 0.000      |
| 0%    | 0.080        | 0.000         | 0.000      | 10.010      | 3.500               | 80.000     | 0.000      |
| 20%   | 20.000       | 0.000         | 0.000      | 22.390      | 4.500               | 90.000     | 0.000      |
| 40%   | 36.000       | 0.000         | 0.000      | 27.130      | 5.700               | 130.000    | 0.000      |
| 50%   | 43.000       | 0.000         | 0.000      | 27.320      | 5.800               | 140.000    | 0.000      |
| 60%   | 49.000       | 0.000         | 0.000      | 27.320      | 6.000               | 155.000    | 0.000      |
| 80%   | 63.000       | 0.000         | 0.000      | 31.070      | 6.500               | 159.000    | 0.000      |
| max   | 80.000       | 1.000         | 1.000      | 95.690      | 9.000               | 300.000    | 1.000      |

Con la finalidad de tener un mayor entendimiento de las variables categoricas se muestra la siguiente tabla.

| diabetes                |    0  |   1 |
|-------------------------|-------|-----|
| gender smoking_history  |       |     |
| Female No Info          |18946  | 754 |
|        current          | 4607  | 451 |
|        ever             | 2027  | 211 |
|        former           | 4125  | 649 |
|        never            |20867  |2002 |
|        not current      | 3519  | 394 |
| Male   No Info          |15410  | 700 |
|        current          | 3731  | 497 |
|        ever             | 1504  | 261 |
|        former           | 3637  | 941 |
|        never            |10879  |1344 |
|        not current      | 2230  | 296 |
| Other  No Info          |    6  |   0 |
|        ever             |    1  |   0 |
|        never            |    3  |   0 |
|        not current      |    8  |   0 |


Para el caso del análisis de las variables individuales se observa que, el promedio de edad es de 41.88 años, en el caso de la hipertensión y cardiopatía es menor al 0.5 (0.075 y 0.039 respectivamente), el índice de masa corporal esta por el 27.32% (por encima del 25 sobrepeso), HbA1c_level con promedio de 5.528, glucosa en sangre de 138.058 y para el caso de la variable objetivo se observa un valor promedio de 0.085 mucho menor al 0.5, dando una idea de la muestra empleada en el estudio.

Es bueno tener en cuenta los diferentes valores y las distribuciones de las variables que pueden resultar significativas en el presente estudio.

Por otra parte, la pivot table muestra como es la relación entre las diferentes variables categóricas.

## Relación entre variables explicativas y variable objetivo

En esta sección se presenta un análisis de la relación entre las variables explicativas y la variable objetivo. Se utilizan gráficos como la matriz de correlación y el diagrama de dispersión para entender mejor la relación entre las variables. Además, se pueden utilizar técnicas como la regresión lineal para modelar la relación entre las variables.
![image](https://github.com/cris21309/tdsp_template_grupo8/assets/162080075/ce199444-7c3b-4a8c-b73c-b4eb467355b6)

Con la finalidad de tener un mayor entendimiento de las posibles variables se ha empelado un gráfico a partir de la correlación de Pearson para las variables numéricas, el analizar los valores, se observa que los mayores valores de correlación se encuentran en 0.40 y 0.42, obteniéndose en la correlación lineal entre el nivel de glucosa con diabetes y HbA1c_level con diabetes, confirmando lo evidenciado en los aparatados anteriores.

