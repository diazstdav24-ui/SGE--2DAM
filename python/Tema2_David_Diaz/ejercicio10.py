"""
Escriba un programa que permita crear una lista de palabras y que, a continuación, elimine los elementos 
repetidos (dejando únicamente el primero de los elementos repetidos). 

"""

palabras = ["a","b","b","a"]
loop = True

copyList = []

if input('¿Escribir una nueva palabra? (s/n): ').lower() != 's':

    loop = False

while loop:
    palabras.append(input('Escribe una palabra: '))
    if input('¿Continuar? (s/n): ').lower() != 's':
        loop = False

for palabra in palabras:
    
    if palabra not in copyList:

        copyList.append(palabra)

        
print(copyList)