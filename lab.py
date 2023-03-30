print("_______________________________________")
print("Programa de registro de infracciones")
print("_______________________________________")

# Pedir al usuario el número total de infracciones reportadas en el mes
numInfracciones = int(input("Ingrese el número total de infracciones reportadas en el mes: "))

# Calcular el número de infracciones en cada período del día
infraccionesManana = int(numInfracciones * 0.2)
infraccionesTarde = int(numInfracciones * 0.35)
infraccionesNoche = numInfracciones - infraccionesManana - infraccionesTarde

# Calcular los promedios diarios de infracciones para cada período del día
promedioManana = infraccionesManana / 30
promedioTarde = infraccionesTarde / 30
promedioNoche = infraccionesNoche / 30

print("El promedio diario de infracciones en horas de la mañana:", round (promedioManana, 2))
print("El promedio diario de infracciones en horas de la tarde:", round (promedioTarde, 2))
print("El promedio diario de infracciones en horas de la noche:", round(promedioNoche, 2))

print("Fin")