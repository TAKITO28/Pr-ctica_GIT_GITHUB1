notas = [14, 16, 11, 18, 13,20,15,16,8]
promedio = sum(notas) / len(notas)
print("Promedio:", promedio)
print("Nota maxima:", max(notas))
print("Nota minima:", min(notas))
print("Cantidad de notas:", len(notas))

from statistics import median

print("Mediana de notas:", median(notas))

if promedio >= 11:
    print("El alumno está aprobado")
else:
    print("El alumno está desaprobado")