# Trabajo Practico Nro 2

## Marco

En el Tp 1 limpiaron y prepararon el dataset de publicaciones de inmuebles de properati. En el Tp 2 vamos a probar algunos modelos lineales sobre el mismo. 

## Objetivos

Contruir al menos tres modelos de regresion lineal y realizar comparativas de las metricas entre los mismos. Se considera modelos diferentes a diferentes tipos de modelos entrenados con los mismos datos o a modelos del mismo tipo entrenados con variables explicativas diferentes. 

## Estructura del trabajo

El trabajo debe comenzar con un breve repaso del dataset donde determinen que columnas desean utilizar en funcion del modelo que decidan armar, chequeen que no incluyan datos invalidos y realicen la ultima limpieza necesaria.
Luego pueden hacer una visualizacion e interpretacion rapida mediante regresiones lineales simples (esto no cuenta como un modelo) para interpretar en nivel de relevancia de cada variable elegida.
A continuacion pueden hacer un modelo de regresion con OLS y statsmodel para comprender el comportamiento del modelo en general y chequear el nivel de relevancia de los coeficientes considerados. Pueden hacer una comparativa de las metricas obtenidas separando correctamente en train/test o train/val los datos y evaluando el R2 y el MSE. Tambien pueden analizar las hipotesis de Gauss-Markov.
Luego la idea es hacer una comparacion con los mismos datos con un modelo que incluya regularizacion para comparar ambos modelos y estudiar si hay o no problemas de sobreajuste. En este tipo de modelos es importante que exploren el espacio de hiperparametros y detecten cual es el nivel optimo de regularizacion interpretando los resultados.
Por ultimo la idea es que armen otro modelo diferente cambiando los datos a utilizar y comparen conclusiones. Este ultimo modelo puede ser una seleccion diferente de columnas o una selecciona diferentes de registros (zona geografica por ejemplo, o tipo de propiedad)

## Sugerencias

- Elegir si el objetivo de la variables a predecir es el valor de una propiedad o el valor del metro cuadrado en una determinada zona/propiedad. 
- Delimitar el area geografica que se desea analizar, se puede realizar un modelo mas generalista abarcando muchas localidades y focalizandose en el valor de la propiedad o realizar un modelo mas especifico que trate de predecir mejor el precio del metro cuadrado en alguna zona con alta densidad de datos. En funcion de esta eleccion tiene sentido usar ciertas columnas u otras.
- Separen correctamente en entrenamiento y testeo. Lo idea serial separar al principio de todo en train/test y luego al realizar pruebas parciales separar en train/validation (o usar validacion cruzada) para ir realizando las pruebas parciales y cuando concluyan probar todo en test. 
- Lleven registro de las cosas que no dieron resultados buenos y tambien reporten esos casos para que poder transmitir todo el proceso de creacion de los modelos y porque hicieron ciertas elecciones basadas en resultados previos. 
- El comportamiento de los modelos es de esperar que varie mucho segun el tipo de propiedad que querramos estudiar, por eso no tiene mucho sentido mezclar los registros de tipos de propiedad diferente. 
