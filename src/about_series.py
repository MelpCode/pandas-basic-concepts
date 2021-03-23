#Data Series
#Una serie es el elemento más basico de Pandas para organizar datos
import numpy as np
import pandas as pd

labels = ['a','b','c']
numbers = [10,20,30]
arr = np.array([100,200,300])
days={'ener':1,'feb':2,'mar':3}

#Se puede crear una serie a partir de una tupla,
#una lista, un arreglo de Numpy y de un diccionario.
#A partir de una diccionario es la forma preferida y más directa

print(pd.Series(numbers))

#Se observa que una Serie se asemeja a una lista, en el sentido
#que los datos se encuentran organizados con un índice: sin embargo, el índice
# esta asociado al dato y no a su posición. De hecho, los índices pueden no
# ser númericos.

print(pd.Series(numbers,index=labels))
print(pd.Series(days))
print(pd.Series(data=labels))

#Se pueden utilizar los keyboards especificos para genera una Serie
serie = pd.Series(data=['PE','CO','CH','BO'],index=['Perú','Colombia','Chile','Bolivia'])
print(serie)

#Una vez definida una Serie, se puede acceder a los datos utlizando el indice como referencia
print(serie['Perú'])

#Tambien se puede llamar a la propiedad con el nombre de los indices
#aunque n es muy usual utilizar esta tecnica pues genera mucha confusion.
#Es por eso que se prefiere utilizar la nomenclatura de indices con [].
print(serie.Colombia)

