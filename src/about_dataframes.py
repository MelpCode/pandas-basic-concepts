# Dataframes
# El Dataframes es la estructura de datos básica de Pandas.
# Se puede considerar que es una colleción de Series de datos organizados
# como una tabla. La mejor forma de entender un Dataframe es utilizar la analogía con una hoja de cálculo
# (Excel por ejemplo) en donde se tienen datos organizados en fila y columnas, donde
# la especificacion de columnas es lo mas relevante.

#Como en el caso de las Series, la forma más sencila de definir un Dataframe es a partir de un diccionario:

import numpy as np
import pandas as pd

df = pd.DataFrame(data=np.random.randint(1,11,(5,4)),
                index=['F1','F2','F3','F4','F5'],
                columns=['C1','C2','C3','C4'])
print(df)
print(type(df))

# Si se extrae una columna del dataframe lo que se obtendra
# será una Serie
# Nota: En un DataFrame no puede extraer datos tomando como referencia los indices.
# a diferencia de una Serie, en el cual si se puede.
ser = df['C1']
print(type(ser))
print(ser)
print(ser['F1'])

# Se pueden extraer las columnas, con lo que se obtendrá un DataFrame
# más pequeño
print(df[['C1','C2']])

# Se pueden agregar columnas a un DataFrame definiendolas 
# directamente (como sucede cuando se quiere agregar una 
# llave más a un diccionario) y se pueden utilizar operaciones 
# con otras columnas. Los operadores soportan "broadcast", es 
# decir, se hace la operación a lo largo de toda la columna.
df['C5'] = df['C3'] + df['C4']
print(df)

#Muchas de las operaciones de Pandas requieren de la especificación de
# de la dirección en la que se van a realizar. utilizando el parametro axis.
df.drop('C5',axis=1) # por defecto axis=0
print(df)

# Un detalle a recordar con las operaciones sobre los 
# DataFrames es que retornan DataFrames, es decir que el 
# DataFrame original se mantiene sin cambios. Para poder 
# establecer el cambio sobre el DataFrame de origien se 
# requiere especificar el keyword `inplace` como `True`
df.drop('C5',axis=1,inplace=True)
print(df)

# El parametro axis puede ser confuso al principio.
# Recuerde que hace referencia a las dimensiones del Dataframe.
# Este dato se puede obtener con el método shape
print(df.shape)



## Ubicacion de los datos por filas
# La informacion de las filas se puede obtener utilizando los 
# métodos `loc` y `iloc`, donde el primero requiere la 
# identificación de los índices, y el segundo la posición de 
# las filas en el DataFrame. `iloc` también soporta 
# index-slincing.
print(df.loc['F2'])
print(df.iloc[1])

print(df.loc['F1','C1']) #interseptamos valores [fila,columna]
print(df.loc[['F1','F2','F3'],['C3','C4']])
print(df.iloc[:2,::])
print(df.iloc[::2,::-2]) 
# ::2 - todas las filas con un salto de 2 en 2
#  ::-2, todas las columnas con un salto de atrás para adelante de 2 en 2.


## INDEXACIÓN BOOLEANA:
# Así como sucede con las listas, un DataFrame soporta operadores
# lógicos para la generación de "mascaras" a utilizar como índices.

df = pd.DataFrame(data=np.random.randint(1, 101, (8, 6)), 
                index=['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8'], 
                columns=['C1', 'C2', 'C3', 'C4', 'C5', 'C6'])
print(df)
print(df>50)
print(df[df>50])
print(df['C1']>50)
print(df[df['C1']>50])
print(df[df['C3']>50])
print(df[df['C3']>50]['C3'])
print('\n')
print(df[(df['C5']>50) & (df['C5'] %7 == 0)]['C5'])


##Control de indices:
df.reset_index()
idx = ['PE','CO','BR','BO','AR','VE','EC','CH']
df['Domain'] = idx
print(df)
df.set_index('Domain') # inplace=True para fijar los cambios
print(df)

## Multiples indices en DataFrames
# Un dataframe puede tener varios niveles de indices utilizando un objeto
# llamado 'MultiIndex'
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2',]
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
print(hier_index)

df = pd.DataFrame(np.random.randn(6, 2), hier_index, ['A', 'B'])
print(df)
print(df.loc['G2'])
print(df.loc['G2']['B'])
print(df.loc['G2']['B'][1])
df.index.names = ['Groups','Num']
print(df)
print(df.loc['G1'])
print(df.xs('G1')) #xs: Cross Section
print(df.xs(2,level='Num'))


## Gestion de datos perdidos
# Cuando se importan datos a un DataFrame puede suceder que 
# los datos tienen errores de formato y no pueden interpretarse 
# de forma correcta. Esto termina con los datos representados 
# como NaN (Not A Number).

# Es necesario gestionar los NaN dentro de un DataFrame para 
# reconocerlos, eliminarlos o reemplazarlos por algun valor 
# (normalmente, por el valor promedio de los otros valores de 
# la misma columna).

d = {'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C':[1, 2, 3]}   
df = pd.DataFrame(d)
print(df)
#df.dropna(inplace=True)
#df.dropna(axis=1,inplace=True)
#df.dropna(thresh=2,inplace=True)
#df.fillna('VALUE',inplace=True)

df['A'].fillna(df['A'].mean(),inplace=True)
df['B'].fillna(df['B'].mean(),inplace=True)
df['C'].fillna(df['C'].mean(),inplace=True)
print(df)


## GROUPBY
# Permite agrupar filas en funcion de una 
# columna y realizar una funcion de agragación en estas

data = {'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
        'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Sales': [200, 120, 340, 124, 243, 350]}

df=pd.DataFrame(data)
print(df)
byCompany =df.groupby('Company')
print(byCompany.mean())
print(byCompany.sum())
print(byCompany.sum().loc['FB'])
print(byCompany.max())
print(byCompany.min())
print(byCompany.describe())
print(byCompany.describe().transpose())
print(byCompany.describe().transpose()['FB'])

## Merge, Join,Concatenate
# Se pueden concatenar (unir) dos DataFrames siempre y cuando 
# se tome en consideración el axis sobre el que se desea 
# trabajar, y que las dimensiones de los DataFrames puedan 
# concordat para realizar la concatenación.

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']},
                        index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']},
                        index=[4, 5, 6, 7])

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                        'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                        'D': ['D8', 'D9', 'D10', 'D11']},
                        index=[8, 9, 10, 11])

newpd = pd.concat([df1,df2,df3])
newpd = pd.concat([df1,df2,df3],axis=1)
print(newpd)

# También se pueden unir dos DataFrames utilizando una columna 
# como referencia. Esto se denomina `merge`

left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']})
print(pd.merge(left,right,on='key'))

#Por otro lado, la operacion join junta dos Dataframes que 
# tengas los mismos indices.
left = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']},
                        index=['K0', 'K1', 'K2', 'K3'])

right = pd.DataFrame({'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']},
                        index=['K0', 'K1', 'K2', 'K3'])
#print(left.join(right))

## Operaciones con Pandas
df = pd.DataFrame({'col1': [1, 2, 3, 4],
                        'col2': [444, 555, 666, 444],
                        'col3': ['abc', 'def', 'ghi', 'xyz']})
print(df)
print(df['col2'].unique())
print(df['col2'].nunique())
print(df['col2'].value_counts())
print(df['col3'].apply(len))
print(df['col1'].apply(lambda x: x**2))
print(df.columns)
print(df.index)
print(df.sort_values('col2'))
print(df.isnull())


## Data Input
# Lectura de archivos csv
df = pd.read_csv('src/notas.csv')
df.set_index('Alumno',inplace=True)
df['PC1'] = df['PC1'].apply(lambda x: x + 3)
print(df)
# Guardar los nuevos datos
# df.to_csv('notas_curva.csv', index=False)

## Lectura de informacion de archivos HTML
data = pd.read_html('https://coinmarketcap.com/currencies/bitcoin/historical-data/')
print(data)

