segundos: int = int(input("Ingrese la cantidad de segundos"))
minutos: int = int(segundos / 60) #Se refunde a int para que python le quite los decimales al resultado.
segundos_faltantes: int = 0

if (segundos % 60 != 0):
    while (segundos % 60 != 0):
        segundos = segundos + 1
        segundos_faltantes = segundos_faltantes + 1
else:
    segundos_faltantes = 60
    print("Los segundos que introdujiste generan " + str(minutos) + " minutos exactos")

print("Faltan " + str(segundos_faltantes) + " segundos para convertirse en exactamente " + str(minutos + 1) + " minutos")
