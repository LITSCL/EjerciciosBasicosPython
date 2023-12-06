largo: int = int(input("Ingrese el largo del rectangulo")) #Se imprime un mensaje, Se lee un str, se convierte a int y se almacena en la variable.
ancho: int = int(input("Ingrese el ancho del rectangulo")) #Se imprime un mensaje, Se lee un str, se convierte a int y se almacena en la variable.

print("El area del rectangulo es: " + str(largo * ancho)) #Se imprime en pantalla la concatenación (Se opera el cálculo y luego se convierte a str para concatenar).
print("El perimetro del rectangulo es: " + str(largo * 2 + ancho * 2)) #Se imprime en pantalla la concatenación (Se opera el cálculo y luego se convierte a str para concatenar).
