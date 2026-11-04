"""
19. Crear un programa que lea los precios de 5 artículos y las cantidades vendidas por una empresa en sus 4
sucursales. Informar de:
    Las cantidades totales de cada artículo.
    La cantidad de artículos en la sucursal 2.
    La cantidad del artículo 3 en la sucursal 1.
    La recaudación total de cada sucursal.
    La recaudación total de la empresa.
    La sucursal de mayor recaudación.
"""

NUM_ARTICULOS = 5
NUM_SUCURSALES = 4

precios = []
cantidades = []   
recaudaciones = []

continuar = True


print('Bienvenido al programa de ventas')

for i in range(1, NUM_ARTICULOS + 1):

    precio = float(input(f'Precio del artículo {i}: '))

    while precio < 0:

        precio = float(input('El precio no puede ser negativo, vuelve a introducirlo: '))

    precios.append(precio)


for s in range(1, NUM_SUCURSALES + 1):

    print(f'\n--- Sucursal {s} ---')

    fila = []

    for a in range(1, NUM_ARTICULOS + 1):

        cantidad = int(input(f'Cantidad vendida del artículo {a}: '))

        while cantidad < 0:

            cantidad = int(input('La cantidad no puede ser negativa, vuelve a introducirla: '))

        fila.append(cantidad)

    cantidades.append(fila)


for fila in cantidades:

    total_sucursal = 0

    for precio, cantidad in zip(precios, fila):

        total_sucursal += precio * cantidad

    recaudaciones.append(total_sucursal)


while continuar:

    opcion = int(input('\n¿Qué desea consultar?\n 1.Cantidades totales de cada artículo\n 2.Cantidad de artículos en la sucursal 2\n '
                       '3.Cantidad del artículo 3 en la sucursal 1\n 4.Recaudación total de cada sucursal\n '
                       '5.Recaudación total de la empresa\n 6.Sucursal de mayor recaudación\n 7.Salir\n'))

    match opcion:

        case 1:

            for a in range(NUM_ARTICULOS):

                total_articulo = 0

                for fila in cantidades:

                    total_articulo += fila[a]

                print(f'Artículo {a + 1}: {total_articulo} unidades')

        case 2:

            print(f'Artículos vendidos en la sucursal 2: {sum(cantidades[1])} unidades')

        case 3:

            print(f'Cantidad del artículo 3 en la sucursal 1: {cantidades[0][2]} unidades')

        case 4:

            for i, recaudacion in enumerate(recaudaciones, start=1):

                print(f'Sucursal {i}: {recaudacion:.2f} €')

        case 5:

            print(f'Recaudación total de la empresa: {sum(recaudaciones):.2f} €')

        case 6:

            mayor = max(recaudaciones)

            print(f'La sucursal de mayor recaudación es la {recaudaciones.index(mayor) + 1} con {mayor:.2f} €')

        case 7:

            print('Hasta luego')

            continuar = False

        case _:

            print('La opción debe estar entre 1 y 7')