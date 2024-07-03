# EJERCICIO VENTAS

from funciones_ventas import *

print('Bievenido a la Almacen-k!')
limpiar_esperar_screen()

opciones = (1, 2, 3, 4, 5)
while True:
    limpiar_esperar_screen()
    opc = menu_opciones((opciones))

    if opc == 1:
        registrar_nueva_venta()
    elif opc == 2:
        reporte_ventas_historico()
    elif opc == 3:
        reporte_ventas_por_prod()
    elif opc == 4:
        reporte_formas_pago()
    else:
        salir()
        break
