"""
Queremos desarrollar un pequeño programa que ayude a un técnico meteorológico (mi amigo Nico es 
meteorólogo) a analizar las temperaturas registradas durante una semana en su estación de trabajo. 
Rellenar la lista con temperaturas generadas de forma aleatoria entre dos límites leídos por teclado. Pueden 
tener decimales. 
A partir de esa lista, el programa debe: 
Mostrar todas las temperaturas introducidas. 
Calcular y mostrar la temperatura media. 
Mostrar la temperatura máxima y mínima junto con el día en que ocurrieron (día 1, día 2, no usar fechas). 
Ordena la lista de mayor a menor temperatura. 
Mostrar cuántos días tuvieron temperaturas por encima de la media. 
Crear una nueva lista solo con las temperaturas superiores a la media. 
"""

import numpy as np

continuar = True


print('Bienvenido a la estación meteorologica')

max = float(input('Diga la temperatura max\n'))
min = float(input('Diga la temperatura min\n'))

temperatura_semanal = []
cont = 1
dias_superiores_media = 0

for i in range(0,7):

    temperatura_semanal.append(float(np.random.randint(min,max)))

media = (sum(temperatura_semanal))/len(temperatura_semanal)

while continuar: 

    opcion = int(input('\n¿Qué desea hacer?\n 1.Mostrar todas las temperaturas\n 2.Ver la media\n ' \
            '3.Ordenar la lista de mayor a menor temperatura\n 4.Mostrar cuantos días tuvieron temperaturas por encima de la media\n '\
            '5.Crear una nueva lista solo con las temperaturas superiores a la media \n'))

    cont = 1

    match opcion: 

        case 1: 

            for temperatura in temperatura_semanal:

                print(f'Dia {cont}: {temperatura}')

                cont += 1

        case 2: 

            print(f'La media es: {media:.2f}')

        case 3: 

            temperatura_ordenada = sorted(temperatura_semanal, reverse=True)

            for temperatura in temperatura_ordenada:

                print(f'Dia {cont}: {temperatura}')
                cont += 1

        case 4: 

            print(f'La media es: {media:.2f}')

            for temperatura in temperatura_semanal:

                if temperatura > media:

                    dias_superiores_media += 1

            print(f'{dias_superiores_media}')

        case 5: 

            superiores_media = []
            print(f'La media es: {media:.2f}')

            for temperatura in temperatura_semanal:

                if temperatura > media:

                        print(temperatura)

                        superiores_media.append(temperatura)
        case __ :

            print('El número introducido no debe de ser superior a 5')
                     


                    
                    



    
