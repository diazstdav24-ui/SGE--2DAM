import shutil


"""
Haz un programa que copie el contenido de un fichero llamado 'origen.txt' en otro llamado 
'copia.txt'
"""
print("Ejercicio 3")


shutil.copyfile("ficheros/fichero1.txt", "ficheros/copia_fichero1.txt")

with open("ficheros/copia_fichero1.txt") as f: 

    print(f.read())


"""
Crea un programa que lea un fichero llamado 'texto.txt' y genere 'numerado.txt' con todas las líneas 
precedidas de su número. 

"""

print("Ejercicio 4")

with open('ficheros/fichero1.txt') as f, open('ficheros/copia_fichero1.txt','w') as j: 

    for i,linea in enumerate(f,start=1):

        j.write(f"{i}.{linea}")


with open('ficheros/copia_fichero1.txt') as f: 

    print(f.read())
        

"""

5. Realiza un programa que lea el fichero 'datos.txt' y cree un nuevo fichero 'invertido.txt' con las 
líneas en orden inverso.
"""

