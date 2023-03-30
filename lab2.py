
print("Bienvenido al programa para determinar que numero es mayor, cual es menor y cual es el de en medio.")

# Solicitar los tres números enteros al usuario
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

# Encontrar el número más grande
if num1 >= num2 and num1 >= num3:
    maxNum = num1
elif num2 >= num1 and num2 >= num3:
    maxNum = num2
else:
    maxNum = num3

# Encontrar el número más pequeño
if num1 <= num2 and num1 <= num3:
    minNum = num1
elif num2 <= num1 and num2 <= num3:
    minNum = num2
else:
    minNum = num3

# Encontrar el número de en medio
medNum = num1 + num2 + num3 - maxNum - minNum

print("El número", maxNum, "es el número más grande de los tres.")
print("El número", minNum, "es el número más pequeño de los tres.")
print("El número", medNum, "es el número de en medio de los tres.")

print("Fin")