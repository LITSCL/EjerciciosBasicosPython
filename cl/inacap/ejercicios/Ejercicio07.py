horas_academicas: float = float(input("Ingrese la cantidad de horas academicas asistidas del alumno:"))
minutos_academicos: float = horas_academicas * 45
horas_reales: float = minutos_academicos / 60
print("La cantidad de horas reales es: " + str(horas_reales))