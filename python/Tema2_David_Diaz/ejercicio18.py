"""
18. En una empresa de transporte se quiere guardar el nombre de los conductores que tiene y los kilómetros
que conducen cada día de la semana. Para guardar esta información se van a utilizar dos listas:
    Nombre: Lista para guardar los nombres de los conductores.
    kms: Tabla para guardar los kilómetros que realizan cada día de la semana.
Se quiere generar una nueva lista ("total_kms") con los kilómetros totales que realiza cada conductor.
Al finalizar se muestra la lista con los nombres de conductores y los kilómetros que ha realizado.
"""

dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

nombres = []
kms = []          
total_kms = []

continuar = True


print('Registro de kilómetros de la empresa de transporte')

while continuar:

    nombre = input(f'\nNombre del conductor {len(nombres) + 1}: ').strip()

    if nombre in nombres:

        print('Ese conductor ya está registrado')

    else:

        nombres.append(nombre)

        kms_conductor = []

        for dia in dias_semana:

            km = float(input(f'Kilómetros de {nombre} el {dia}: '))

            while km < 0:

                km = float(input('Los kilómetros no pueden ser negativos, vuelve a introducirlos: '))

            kms_conductor.append(km)

        kms.append(kms_conductor)

    if input('¿Desea añadir otro conductor? (s/n): ').lower().strip() != 's':

        continuar = False


for fila in kms:

    total_kms.append(sum(fila))


print('\nConductor | Kilómetros totales')

for nombre, total in zip(nombres, total_kms):

    print(f'{nombre} | {total:.2f} km')