evaluacion_1: float = float(input("Ingrese la nota de la primera evaluacion")) #Se muestra un str, se lee un str, se convierte a float y se almacena en la variable.
evaluacion_2: float = float(input("Ingrese la nota de la segunda evaluacion")) #Se muestra un str, se lee un str, se convierte a float y se almacena en la variable.
evaluacion_3: float = float(input("Ingrese la nota de la tercera evaluacion")) #Se muestra un str, se lee un str, se convierte a float y se almacena en la variable.
evaluacion_4: float = float(input("Ingrese la nota de la cuarta evaluacion")) #Se muestra un str, se lee un str, se convierte a float y se almacena en la variable.

print("El promedio final del alumno es: " + str(evaluacion_1 * 0.15 + evaluacion_2 * 0.20 + evaluacion_3 * 0.25 + evaluacion_4 * 0.40)) #Se imprime en pantalla la concatenación.
