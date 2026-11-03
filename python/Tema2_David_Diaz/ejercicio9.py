"""
Escriba un programa que permita crear una lista de palabras y que, a continuación, cree una segunda lista 
igual a la primera, pero al revés (no se trata de escribir la lista al revés, sino de crear una lista distinta).
"""

continuar = True
words = []


while continuar: 

    words.append(input('write a word '))

    option = int(input('continue? 1.y|2.n '))

    if option == 2:

        continuar = False

copy = list.copy()

copy = reversed(copy)


print(', '.join(words))

print(', '.join(copy))


## Version simplificada de mi codigo hecho por la IA 

palabras = []

while True:
    palabras.append(input('Escribe una palabra: '))
    if input('¿Continuar? (s/n): ').lower() != 's':
        break

invertida = list(reversed(palabras))

print(palabras)
print(invertida)

##Con reverse 

palabras = []

while True:
    palabras.append(input('Escribe una palabra: '))
    if input('¿Continuar? (s/n): ').lower() != 's':
        break

invertida = palabras.copy()
invertida.reverse()

print(palabras)
print(invertida)