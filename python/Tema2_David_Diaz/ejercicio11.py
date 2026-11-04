"""
Escriba un programa que permita crear dos listas de palabras y que, a continuación, escriba las siguientes 
listas (en las que no debe haber repeticiones): 
    Lista de palabras que aparecen en las dos listas. 
    Lista de palabras que aparecen en la primera lista, pero no en la segunda. 
    Lista de palabras que aparecen en la segunda lista, pero no en la primera. 
    Lista de palabras que aparecen en ambas listas.
"""


loop = True

list_words1= ['Hola', 'Adios', 'A','B']
list_words2=['Hola', 'David', 'A','C']
newList = []
newList2 = []


if int(input('¿Desa añadir una nueva palabra? 1.Y/2.N ' )) == 2:

    loop = False


while loop: 

    word = input('Nueva palabra lista 1: ')

    if word in list_words1:
        
        print('La palabra ya se encuentra en la lista 1 ')        

    list_words1.append(word)

    word = input('Nueva palabra lista 2: ')

    if word in list_words2: 

        print('La palabra ya se encuentra en la lista 1 ')        

    
    list_words2.append(word)

    if int(input('¿Desea continuar? 1.Y/2.N' == 2)):

        loop = False



for word1, word2 in zip(list_words1,list_words2):

    if word1 in list_words2:


        newList.append(word1)

print('Lista de palabras que aparecen en las dos listas: ')
print(newList)

newList.clear()

for word1, word2 in zip(list_words1,list_words2):

    if word1 not in list_words2:

        newList.append(word1)

    if word2 not in list_words1:

        newList2.append(word2)

print('    Lista de palabras que aparecen en la primera lista, pero no en la segunda. ')
print(newList)

print('Lista de palabras que aparecen en la segunda lista, pero no en la primera. ')
print(newList2)


#Forma phytonica de la IA 

"""
Programa que pide dos listas de palabras y muestra, sin repeticiones:
- Las palabras que aparecen en las dos listas
- Las que aparecen en la primera pero no en la segunda
- Las que aparecen en la segunda pero no en la primera
- Las que aparecen en alguna de las dos
"""


def pedir_palabras(numero):
    palabras = []
    print(f'--- Lista {numero} (pulsa Enter sin escribir nada para terminar) ---')
    while True:
        palabra = input('Nueva palabra: ').strip()
        if palabra == '':
            break
        if palabra in palabras:
            print(f'La palabra ya se encuentra en la lista {numero}')
        else:
            palabras.append(palabra)
    return palabras


lista1 = pedir_palabras(1)
lista2 = pedir_palabras(2)

en_las_dos = [palabra for palabra in lista1 if palabra in lista2]
solo_en_1 = [palabra for palabra in lista1 if palabra not in lista2]
solo_en_2 = [palabra for palabra in lista2 if palabra not in lista1]
en_alguna = lista1 + solo_en_2

print('Palabras que aparecen en las dos listas:', sorted(en_las_dos))
print('Palabras de la primera que no están en la segunda:', sorted(solo_en_1))
print('Palabras de la segunda que no están en la primera:', sorted(solo_en_2))
print('Palabras que aparecen en alguna de las dos:', sorted(en_alguna))

    
