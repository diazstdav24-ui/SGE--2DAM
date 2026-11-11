"""
3. Crear un diccionario que tenga como claves el dni de un estudiante y como valor la nota media de su 
expediente. La nota media se generará de manera aleatoria entre 1 y 10. 
 
Escribir el código necesario en un menú para hacer los siguiente: 
 
a) Mostrar los datos. 
b) Modificar la nota. 
c) Añadir un nuevo estudiante. 
d) Crear un nuevo diccionario (no modificar el original) solo con los estudiantes que tienen nota media 
mayor a un valor dado por teclado (por ejemplo, para comprobar que pueden entrar en un ciclo según esa 
nota de corte)

"""
import numpy as np 

loop = True


diccionario = {}

diccionario_media = {}

while loop:
    
    dni = input('Diga el DNI del mismo: ')

    diccionario.setdefault(dni,float(np.random.randint(0.0,10.0)))

    salir = int(input('¿Seguir? 1.Y/2.N'))

    if salir == 2: 

       loop = False


loop = True


while loop:

    opcion = int(input('1 mostrar los datos\n2.Modificar la nota\n3.Añadir un nuevo estudiante'+
                       '\n4.Crear un nuevo diccionario con estudiantes mayor a la media\n0.Salir'))

    match opcion: 

        case 1: 

         print(diccionario)

        case 2: 

            dni = input('Cual es el dni')

            diccionario.get(dni)

            nota = None

            while nota == None:

                nota = float(input('¿Qué nota deseas colocar, entre 0 y 10'))

                nota = nota if 0.0 <= nota <= 10.0 else None

            diccionario[dni] = nota

            print(diccionario)

        case 3: 


            while True:
        
                dni = input('Diga el dni del nuevo estudiante')

                if dni in diccionario:

                    print('Este dni ya se encuentra en el diccionario')

                break

            diccionario.setdefault(dni,float(np.random.randint(0.0,10.0)))

            print(diccionario)

        case 4: 

            nota = None

            while nota == None:
                    
                notaMedia = float(input('Diga la nota media'))

                notaMedia = notaMedia if 0.0 <= notaMedia <= 10.0 else None

                for dni, nota in diccionario.items():
                    
                    if notaMedia <= nota:

                        diccionario_media.setdefault(dni,nota)

                print(diccionario_media)

        case 0: 

            print('adios') 

            loop = False

        case _ : 

            print('Debe de estar entre 0-5')               







