"""
Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y elimine 
esa palabra de la lista.
"""

words = ["Hola","Alejandro","Betis"]

continuar = True

while continuar:

    word = input('Qué palabras quieres eliminar de la lista \n')

    if word in words: 

        words.remove(word)

        print(f'La palabra: {word} ha sido borrado \n')

        print('\n'.join(words))

        continuar = False

    else: 

        print('La palabra tiene que estar en la lista')

