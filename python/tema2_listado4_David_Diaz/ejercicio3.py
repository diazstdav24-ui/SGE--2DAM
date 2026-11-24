import shutil


"""
Haz un programa que copie el contenido de un fichero llamado 'origen.txt' en otro llamado 
'copia.txt'
"""

shutil.copyfile("ficheros/fichero1.txt", "ficheros/copia_fichero1.txt")

with open("ficheros/copia_fichero1.txt") as f: 

    print(f.read())

