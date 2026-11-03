"""
6. Escriba un programa que permita crear una lista de palabras y que, a continuación, pida dos palabras y 
sustituya la primera por la segunda en la lista.

"""


continuar = True
palabras = []
cont = 1

while continuar: 

    palabras.append(input('Diga la palabra que va a insertar \n'))

    opcion = int(input('¿Desea insertar otra? 1.S/2.N \n'))

    if opcion == 2: 

        continuar = False

print('\n'.join(palabras))



for i in range(2):

    palabra = input(f'Di la palabra número {cont}')

    if i == 0: 

        palabras.pop(1)
        palabras.insert(1, palabra)

    cont += 1

print('\n'.join(palabras))







            