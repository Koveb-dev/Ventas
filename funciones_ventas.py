import csv
import time
import os

titulos = ["Producto", "Cantidad", "Valor unitario",
           "Forma de pago", "Precio Total"]
ventas = []
medios_pago = ("Efectivo", "Debito", "Credito", "Transferencia electronica")
try:
    with open("ventas.csv", "x", newline="")as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(titulos)
except:
    pass


def menu_opciones(p_opcs):
    while True:
        print('\tMenú Almacen\n\n\t1. Registrar nueva venta\n\t2. Reporte de ventas historico\n\t3. Reporte de ventas por producto\n\t4. Reporte por formas de pago\n\t5. Salir\n')
        try:
            opc = int(input('\tIngrese una opción: '))
            if opc in p_opcs:
                return opc
            else:
                print(
                    'ERROR! debe ingresar una opción valida, opciones validas (1,2,3,4,5)!')
            limpiar_esperar_screen()
        except:
            print('ERROR! debe ingresar un número entero!')


def registrar_nueva_venta():
    print('Registrar venta!')
    limpiar_esperar_screen()

    while True:
        nombre_producto = str(input('Ingrese el nombre del producto: '))
        if len(nombre_producto.strip()) >= 3:
            print('Nombre ingresado correctamente!')
            limpiar_esperar_screen()
            break
        else:
            print('ERROR! debe ingresar nombre que contenga al menos 3 caracteres!')
        limpiar_esperar_screen()

    while True:
        try:
            cantidad_producto = int(
                input(f'Ingrese la cantidad {nombre_producto}: '))
            if cantidad_producto >= 1 and cantidad_producto <= 10000:
                print('Cantidad ingresada correctamente!')
                limpiar_esperar_screen()
                break
            else:
                print(
                    'ERROR! debe ingresar una cantidad valida que este dentro del rango de 1 a 10.000!')
            limpiar_esperar_screen()
        except:
            print('ERROR! debe ingresar un número entero!')

    while True:
        try:
            valor_uni_producto = int(
                input('Ingrese el valor unitario del producto: '))
            if valor_uni_producto >= 100:
                print('Valor unitario ingresado correctamente!')
                limpiar_esperar_screen()
                break
            else:
                print(
                    'ERROR! el valor de unitario del producto debe valer como minimo $100 clp!')
            limpiar_esperar_screen()
        except:
            print('ERROR! debe ingresar un numero entero!')

    while True:
        try:
            opciones_pago = int(input(
                'Ingrese el medio de pago (1: Efectivo 2: Debito 3: Credito 4: Tranferencia electronica): '))
            if opciones_pago in (1, 2, 3, 4):
                print('Medio de pago ingresado correctamente!')
                limpiar_esperar_screen()
                break
            else:
                print(
                    'ERROR! debe ingresar un medio de pago valido, medios de pago validos (1,2,3,4)!')
            limpiar_esperar_screen()
        except:
            print('ERROR! debe ingresar un número entero!')

    p_total_prod = int(cantidad_producto * valor_uni_producto)

    cont_efectivo = 0
    cont_debito = 0
    cont_credito = 0
    cont_t_electronica = 0

    monto_total_efect = 0
    monto_total_debito = 0
    monto_total_credito = 0
    monto_total_t_electronica = 0

    if opciones_pago == 1:
        cont_efectivo = cont_efectivo + 1
        monto_total_efect = monto_total_efect + p_total_prod
    elif opciones_pago == 2:
        cont_debito = cont_debito + 1
        monto_total_debito = monto_total_debito + p_total_prod
    elif opciones_pago == 3:
        cont_credito = cont_credito + 1
        monto_total_credito = monto_total_credito + p_total_prod
    else:
        cont_t_electronica = cont_t_electronica + 1
        monto_total_t_electronica = monto_total_t_electronica + p_total_prod

    venta = [nombre_producto, cantidad_producto,
             valor_uni_producto, medios_pago[opciones_pago-1], p_total_prod]

    ventas.append(venta)
    print('VENTA REGISTRADA!')
    limpiar_esperar_screen()

    with open("ventas.csv", "a", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(ventas)
    print('ARCHIVO CREADO!')


def reporte_ventas_historico():
    print('Reporte de ventas historico!')
    limpiar_esperar_screen()

    if len(ventas) >= 1:
        while True:
            print('\tVentas realizadas\n')
            for l in ventas:
                print(
                    f"Producto: {l[0]}\tCantidad: {l[1]}\tValor unitario: {l[2]}\tForma de pago: {l[3]}\tPrecio Total: {l[4]}\n")
            opc_salir = str(
                input('¿Deseas salir? Ingrese ("s":salir "n":redirigir): '))
            if opc_salir.lower() in ("s", "n"):
                if opc_salir.lower() == "s":
                    print('saliendo.')
                    limpiar_esperar_screen()
                    break
                else:
                    print('redirigiendo.')
                limpiar_esperar_screen()
            else:
                print(
                    'ERROR! debe ingresar una opción valida, opciones validas("s" o "n")!')
    else:
        print('NO HAY VENTAS REGISTRADAS!')
    limpiar_esperar_screen()


def reporte_ventas_por_prod():
    print('Reporte de ventas por producto!')
    limpiar_esperar_screen()
    if len(ventas) >= 1:
        titulos_producto = ["producto", "cantidad vendida", "Monto vendido"]
        matriz = []
        while True:
            with open("ventas_producto.csv", "w", newline="") as archivo:
                escritor = csv.writer(archivo)
                escritor.writerow(titulos_producto)
                print(titulos_producto)
                for i in ventas:
                    print(f" {i[0]}\t\t  {i[1]}\t\t  ${i[4]}\n\t")
                    lista = [i[0], i[1], i[4]]
                    matriz.append(lista)
                escritor.writerows(matriz)
            print("Archivo Creado")

            opc_salir = str(
                input('¿Desea salir? Ingrese ("S":salir "N":redirigir): '))
            if opc_salir.upper() in ("S", "N"):
                if opc_salir.upper() == "S":
                    print("Saliendo.")
                    limpiar_esperar_screen()
                    break
                else:
                    print('Redirigiendo.')
                limpiar_esperar_screen()
            else:
                print(
                    'ERROR! debe ingresar una opcion valida, opciones validas ("S" o "N")!')
            limpiar_esperar_screen()

    else:
        print('NO HAY VENTAS REGISTRADAS!')
    limpiar_esperar_screen()


def reporte_formas_pago():
    print('Reporte de formas de pago!')
    limpiar_esperar_screen()

    if len(ventas) >= 1:
        titulos_medios_pago = ["forma de pago",
                               "cantidad vendida", "Monto vendido"]

        while True:
            matriz = []
            with open("ventas_producto.csv", "w", newline="") as archivo:
                escritor = csv.writer(archivo)
                escritor.writerow(titulos_medios_pago)
                print(titulos_medios_pago)
                for i in ventas:
                    print(f" {i[0]}\t\t  {i[1]}\t\t  ${i[4]}\n\t")
                    lista = [i[0], i[1], i[4]]
                    matriz.append(lista)
                escritor.writerows(matriz)
            print("Archivo Creado")

            opc_salir = str(
                input('¿Desea salir? Ingrese ("S":salir "N":redirigir): '))
            if opc_salir.upper() in ("S", "N"):
                if opc_salir.upper() == "S":
                    print("Saliendo.")
                    limpiar_esperar_screen()
                    break
                else:
                    print('Redirigiendo.')
                limpiar_esperar_screen()
            else:
                print(
                    'ERROR! debe ingresar una opcion valida, opciones validas ("S" o "N")!')
            limpiar_esperar_screen()
    else:
        print('NO HAY VENTAS REGISTRADAS!')
    limpiar_esperar_screen()


def limpiar_esperar_screen():
    time.sleep(1)
    os.system('cls')


def salir():
    for i in range(1, 4):
        print('Saliendo de Almacen-k', ("."*i))
        limpiar_esperar_screen()


# Superstar - Painting Pictures Live Mic Performance
