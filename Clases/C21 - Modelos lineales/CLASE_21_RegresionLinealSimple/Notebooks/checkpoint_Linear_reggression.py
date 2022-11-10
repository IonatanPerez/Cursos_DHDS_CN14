import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from PIL import Image
import requests
from io import BytesIO
import sys
sys.path.insert(1, '../../../common')
from checkpoint import *

descripcion_1 = '''
La regresión lineal es un algoritmo No supervisado de aprendizaje automático.
'''
opciones_1 = ['Verdadero', 'Falso']
feedback_1 = ['¿Que quiere decir supervisado? Recuerda que uno de los algotimos de aprendizaje no tenia en cuenta  etiquetas para el entrenamiento y el otro si','¡Muy bien! Sí, la regresión lineal es un algoritmo de aprendizaje supervisado porque utiliza etiquetas verdaderas para el entrenamiento. El algoritmo de aprendizaje supervisado debe tener una variable de entrada (x) y una variable de salida (Y) para cada ejemplo.']
test_1 = create_multiple_choice(descripcion_1, opciones_1, 'Falso', feedback_1)

descripcion_2 = '''
¿Cuál de los siguientes métodos usamos para encontrar la mejor recta de ajuste para datos en Regresión lineal?
'''
opciones_2 = ['Mínimos cuadrados ordinarios (MCO)',
              'Máxima verosimilitud',
              'Funcion de perdida logaritmica',
              'A y B son correctas.']
feedback_2 = ['Por supuesto!!.En la regresión lineal, tratamos de minimizar los errores de mínimos cuadrados del modelo para identificar la línea de mejor ajuste.',
              'Intentemos de nuevo',
              'Esta función de costo es la famosa log loss para clasificación',
              'Seguro que es la maxima verosimilitud?']
test_2 = create_multiple_choice(descripcion_2, opciones_2, opciones_2[0], feedback=feedback_2)

descripcion_3 = '''
¿Cuál de los siguientes enunciados es cierto acerca de los residuos?
'''
opciones_3 = ['Mientras mas grande mejor','Mientras mas chicos mejor','no se puede determinar con la informacion disponible','ninguna de la anteriores']
feedback_3 = ['Recuerda que el residuo es la diferencia entre el y verdadero y el y predicho',
              'Genial!. Los residuos se refieren a los valores de error del modelo. La diferencia entre el valor real y el predicho. Por lo tanto, se desean residuos bajos.',         'Recuerda que el residuo es la diferencia entre el y verdadero y el y predicho',
              'Recuerda que el residuo es la diferencia entre el y verdadero y el y predicho',]

test_3 = create_multiple_choice(descripcion_3, opciones_3, opciones_3[1], feedback=feedback_3)

descripcion_4 = '''
Dado dos  variables x1 y x2 que siguen la siguiente relacion. ¿Son colineales?
'''
opciones_4 = ['Sí.', 'No.']
feedback_4 = ['Correcto! La colinealidad es la propiedad según la cual un conjunto de puntos están situados sobre la misma línea recta.',
              'Que quiere decir Colineal? ']


def test_4():
    x = np.arange(100)
    delta = np.random.uniform(-5,5, size=(100,))
    y = .4 * x +3 + delta
    fig = plt.figure(figsize=(8, 8))
    plt.scatter(x, y, c=y, cmap='rainbow')
    plt.xlabel('x1')
    plt.ylabel('x2')
    create_multiple_choice(descripcion_4, opciones_4, 'Sí.', feedback_4, fig=fig)()


descripcion_5 = """
Suponga que tenemos N variables independientes (X1, X2 ... Xn) y que la variable dependiente es Y. Ahora imagine que está aplicando una regresión lineal ajustando la mejor línea de ajuste usando el mínimo error cuadratico en estos datos.


A continuación descubrió que el coeficiente de correlación para una de sus variables (Digamos X1) con Y es -0.95.
"""
opciones_5 = [
    'La relación entre X1 e Y es débil.',
    'La relación entre X1 e Y es fuerte',
    'La relación entre X1 e Y es neutral',
    'La correlación no puede evaluar la relación entre las variables.'
]

feedback_5 = [
    '''
    La correlacion (en numeros absolutos) alude a la proporcionalidad y la relación lineal que existe entre distintas variables.
    ''',
    '''
    ¡Muy Bien! El valor absoluto del coeficiente de correlación denota la fuerza de la relación. Como la correlación absoluta es muy alta, significa que la relación es fuerte entre X1 e Y.
    ''',
    '''
    La correlacion (en numeros absolutos) alude a la proporcionalidad y la relación lineal que existe entre distintas variables.
    ''',
    '''
    La correlacion (en numeros absolutos) alude a la proporcionalidad y la relación lineal que existe entre distintas variables.
    '''
]
test_5 = create_multiple_choice(descripcion_5, opciones_5, opciones_5[1], feedback_5)

descripcion_6 = '''
El siguiente grafico que muestra la relación entre x,y. ¿Cumple con el supuesto de homocedasticidad?
'''
opciones_6 = ['Si.',
              'No.']
feedback_6 = ['¡Revisá los supuestos de la regresión lineal!','Correcto!En estadística, una secuencia de variables aleatorias cumple el supuesto de homocedasticidad si todas sus variables aleatorias tienen la misma varianza finita. Esto también se conoce como homogeneidad de varianza']

def test_6():
    response = requests.get('https://ars.els-cdn.com/content/image/3-s2.0-B9780128104842000104-f10-29-9780128104842.jpg?_')
    img = Image.open(BytesIO(response.content))
    basewidth = 350
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    display(img)
    create_multiple_choice(descripcion_6, opciones_6, opciones_6[1], feedback_6)()