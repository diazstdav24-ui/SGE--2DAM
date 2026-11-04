"""
12. Escriba un programa que permita crear una lista de palabras y que, a continuación, ordene la lista por orden 
alfabético.

"""

loop = True

list_word = ['David','Alejandro','Claudia','Thiago']

if int(input('¿Deseas añadir una palabra a lista? 1.Y/2.N: ')) == 2: 

    loop = False


while loop: 

    word = input('Palabra a añadir: ')

    list_word.append(word)

    if int(input('¿Desea continuar? 1.Y/2.N')) == 2:

        loop = False


print(sorted(list_word))

    