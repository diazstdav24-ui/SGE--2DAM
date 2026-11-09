# Diccionarios

- Mantienen el orden de inserccion de las claves
- Son mutables
- Las claves deben ser unicas, pero lo valores si se pueden repetir

En terminos de Big O es bastante rapida

```python

empty_dict = {}
rae = {
  bifronte :  De dos frentes o dos caras ,
  anarcoide :  Que tiende al desorden ,
  montuvio :  Campesino de la costa
 }


```

## Conversión

```python

dict([ a1 ,  b2 ])
{ a :  1 ,  b :  2 }
>>> # Diccionario a partir de una tupla de cadenas de texto
>>> dict(( a1 ,  b2 ))
{ a :  1 ,  b :  2 }
>>> # Diccionario a partir de una lista de listas
>>> dict([[ a , 1], [ b , 2]])
{ a : 1,  b : 2}

```

## get()

Sirve para buscar por clave

```python

>>> rae
2 { bifronte :  De dos frentes o dos caras ,
3  anarcoide :  Que tiende al desorden ,
4  montuvio :  Campesino de la costa }
5
6 >>> rae.get( bifronte )
7  De dos frentes o dos caras
8
9 >>> rae.get( programación )


```

## Obtener todos los elementos:

Por clave:
`rae.keys()`
devuelve :
`dict_keys([ bifronte ,  anarcoide ,  montuvio ,  enjuiciar ])`

Por valor:
`rae.values()`
devuvle:
`dict_values([De dos frentes o dos caras ,que tiende al desorden ,`

Para traerme todo:

```python

rae.items()
dict_items([
( bifronte ,  De dos frentes o dos caras ),
( anarcoide ,  Que tiende al desorden ),
( montuvio ,  Campesino de la costa ),
( enjuiciar ,  Instruir, juzgar o sentenciar una causa )
])


```
