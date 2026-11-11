"""

5. Crea un conjunto de números enteros leyendo por teclado. Se podrá hacer lo siguiente: 
 
1. Añadir el número 15. 
2. Eliminar el número 9. 
3. Calcular la cantidad de elementos. 
4. Comprobar si 6 está en el conjunto. 
 
"""

conjunto = set()

loop = True

while loop: 
    
    conjunto.add(int(input("Diga el número que quieres añadir ")))

    loop = True if int(input('¿Continuar añadiendo 1.Y/2.N? ')) == 1 else False 


loop = True 

while loop: 

    opcion = int(input('¿Qué desea hacer? 1.Añadir el número 15 2.Eliminar el número 9 3.Calcular la cantidad de elementos 4.Comprobar si está el 6 en el conjunto 0.Salir '))

    match opcion: 

        case 1: 

            conjunto.add(15)

            print(conjunto)

        case 2: 

            conjunto.remove(9)
            
            print(conjunto)

        case 3: 

            print(sum(conjunto))
 

        case 4: 

         se_encuentra = True if 6 in conjunto else False

         print(se_encuentra)

        case 0: 

            loop = False

        case _: 

             print('El número debe de estar entre 0 y 4')
                
        

    
