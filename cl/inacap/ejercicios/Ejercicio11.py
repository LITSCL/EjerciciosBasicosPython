numero_1: int = int(input("Ingrese el primer numero")) #Se imprime un mensaje, Se lee un str, se convierte a int y se almacena en la variable.

print("Ingrese el segundo numero")
numero_2: int = int(input()) #Se lee un str y se convierte a int.

print("Los numeros que estan entre " + str(numero_1) + " y " + str(numero_2)) #Se imprime en pantalla la concatenación.

if (numero_1 < numero_2): #Se evalua la condicion.
    contador_1: int = numero_1 + 1
    contador_2: int = 0
    for i in range((numero_2 - numero_1) - 1): #Se repite la cantidad de veces indicada en el valor del parámetro.
        print(contador_1)
        contador_1+=1
        contador_2+=1
else:
    contador_1: int = numero_2 + 1
    contador_2: int = 0
    for i in range((numero_1 - numero_2) - 1): #Se repite la cantidad de veces indicada en el valor del parámetro.
        print(contador_1)
        contador_1+=1
        contador_2+=1
        
print("La cantidad de numeros que hay entre " + str(numero_1) + " y " + str(numero_2) + " son: " + str(contador_2) + " numeros") #Una vez fuera de la condición se ejecuta esta instrucción.
        
        