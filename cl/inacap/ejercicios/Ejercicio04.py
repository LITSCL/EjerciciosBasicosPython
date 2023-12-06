precio_venta: float = float(input("Ingrese el precio de la venta")) #Se lee un str y se convierte a float.

if (precio_venta > 300000): #Se evalua la condición.
    precio_venta = precio_venta * 0.90 #Se realiza un descuento de 10%.
    precio_venta = precio_venta * 1.19 #Se le agrega el IVA.
    print("El precio de la venta con el IVA es: " + str(precio_venta)) #Se imprime en consola la concatenación.
else:
    precio_venta = precio_venta * 1.19
    print("El precio de la venta con el IVA es: " + str(precio_venta)) #Se imprime en consola la concatenación.

