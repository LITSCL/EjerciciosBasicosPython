contador: int = 0 #Se declara una variable y se almacena un int.
suma: int = 0

for i in range(100): #Se declara un bucle for que repite 100 iteraciones.
    contador+=1 #Al contador se le aumenta en una unidad.
    suma = suma + contador #A cada iteracion a la variable se le suma el contador.

print("La suma de los primeros 100 numeros naturales es: " + str(suma)) #Se imprime en consola la concatenación.