
from datetime import datetime
"""
Escribe un programa que cuente cuántas líneas NO vacías contiene un fichero 
'entrada.txt' que tenga varias líneas de prueba.
"""

f = open('ficheros/fichero1.txt')

lista = f.readlines()
count = 0

for linea in lista: 


    if linea != '\n':

        count = count + 1
        

print(count)

f.close()

"""
Crea un programa que añada la fecha y hora actuales al final de un fichero.

"""


fechaYHora = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
with  open('ficheros/fichero1.txt', 'a') as f: 
    f.write(f" \n {fechaYHora}")

with open('ficheros/fichero1.txt') as f: 

        print(f.read())
 

