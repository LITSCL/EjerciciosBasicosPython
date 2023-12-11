numero_1: int = int(input("Ingrese el primer numero"))
numero_2: int = int(input("Ingrese el segundo numero"))

if (numero_1 > numero_2): #Se evalúa la condición.
    print("El primer numero es mayor que el segundo") 
elif (numero_1 < numero_2):
    print("El segundo numero es mayor que el primero") #Si la condición se cumple, imprime el contenido e ignora las demás condiciones.
else:
    print("Ambos numeros son iguales") #Si ninguna condición se cumplio se imprime el contenido del else.