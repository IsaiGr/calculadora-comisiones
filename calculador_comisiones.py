#tengo que calcular las comisiones de las ventas totales de los vendedores que la comision es del 13%
#ingreso de datos
nombre_vendedor = input("Nombre: ")
ventas = input("ingrese dinero total de ventas: ")

ventas = int (ventas)
comision = ventas * 13 / 100
comision = round(comision)
print(f"hola {nombre_vendedor}, tus comisiones son de $ {comision}")






