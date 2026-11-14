"""
Voy a alquilar una habitación de mi casa a modo de apartamento turístico y necesito un programa para gestionar lo 
recaudado. Se debe usar una lista como estructura principal para guardar los datos (si hace falta alguna tupla se puede 
usar). Como no hemos dado todavía objetos, lo haremos con una lista de flotantes, que será lo recaudado cada día que lo 
alquilo. 
El programa puede empezar creando una lista directamente con datos y luego poder hacer lo siguiente mediante un menú 
en la clase Principal y debe mostrar en la misma 
• Agregar una nueva recaudación. 
• Poner a cero una recaudación (se me ha ido el cliente sin pagar). 
• Imprimir toda la lista, es decir, mostrar todos los datos de todas las recaudaciones en bonito. 
• Buscar el día en que más he ganado y decir cuántos días he ganado esa cantidad. 
• Sumar una cantidad a un día como gasto extra. 
• Calcular cuánto he recaudado en todas las recaudaciones. 
• Ordenar la lista de mayor a menor. 
• Calcular la media diaria. 
• Calcular el porcentaje de días al mes (suponiendo 30 días) en que he tenido la habitación alquilada. 
• Dividir la lista en dos nuevas listas. Una de ellas debe ser la que tenga las 5 menores recaudaciones, la otra las restantes.
"""


recaudado = [
    100.0, 90.0, 55.0,
    120.5, 45.0, 80.75, 210.0, 65.2,
    150.0, 30.5, 95.0, 175.8, 110.0,
    60.0, 140.25, 85.0, 195.5, 50.0
]


loop = True



while loop: 

    option = int(input('\n¿Qué desea hacer? \n1.Agregar una nueva recaudación \n2.Poner a cero una recaudación \n3.Imprimir toda la lista'+
                   ' \n4.Buscar el dia que más he ganado \n5.Sumar una cantidad a un día como gasto extra \n6.Calcular el total '+
                   '\n7.Ordenar de mayor a menor \n8.Media díaria \n9.Calcular el porcentaje de días alquilada \n0.Dividir la lista en dos nuevas listas \nf.Para salir ')
                   )

    match option: 
        case 1: 

            recaudado.append(float(input('¿Cuanto quieres añadir?: ')))
            print(recaudado + '\n')

        case 2:

            recaudacion = float(input('Diga la recaudación que deseas poner a cero: '))

            index = recaudado.index(recaudacion)

            recaudado.remove(recaudacion)

            recaudado.insert(index, 0.0)

            print(recaudado)

        case 3: 

            for recaudacion in recaudado: 

                cont = 1

                print(f'Día {cont}: {recaudacion}')

                cont += 1

        case 4: 

            print(max(recaudado))

        case 5: 


            index = recaudado.index(float(input('¿Qué cantidad quieres seleccionar?')))

            recaudacion = recaudado.pop(index)

            recaudacion += float(input('¿Cuanto quieres añadir?'))

            recaudado.insert(index, recaudacion)

            print(recaudado)

        
        case 6: 

            print(sum(recaudado))

        case 7: 

            print(sorted(recaudado, reverse=True))

        case 8: 

            media = sum(recaudado)/len(recaudado)

            print(f'Media: {media:.2f}')

        case 9: 

            porcentaje = len(recaudado)/30 * 100
            print(f'Porcentaje de días: {porcentaje}')

        case 0: 

            ordenada = sorted(recaudado)

            menoresRecaudacion = ordenada[:5]

            mayoresRecaudacion = ordenada[5:]

            print(menoresRecaudacion)

            print(mayoresRecaudacion)
            
        case f : 

            