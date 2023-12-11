precio_venta: float = float(input("Ingrese el precio de la venta")) #Se lee un str, se convierte a float y se almacena en la variable.

if (precio_venta > 500000): #Se evalua la condición.
    precio_venta = precio_venta * 0.90
else:
    precio_venta = precio_venta * 0.95

print("El precio de la venta con el IVA incluido es: " + str(precio_venta * 1.19)) #Se imprime en consola la siguiente conactenación.