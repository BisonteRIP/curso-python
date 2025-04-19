###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales


num1 = int(input("Coloca el primer número\n"))
num2 = int(input("Coloca el segundo número\n"))

# Intentar convertir las entradas a números
try:
    if num1 > num2:
        print(f"{num1} es mayor que {num2}")
    elif num1 < num2:
        print(f"{num2} es mayor que {num1}")
    else:
        print(f"{num1} y {num2} son iguales")
except ValueError:
    print("El dato ingresado no es un número válido")


# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

num1 = int(input("Coloca el primer número\n"))
num2 = int(input("Coloca el segundo número\n"))
operacion = input("Coloca una operacion")

if operacion == "+":
    print(num1 + num2)
elif operacion == "-":
    print(num1 - num2)
elif operacion == "*":
    print(num1 * num2)
elif operacion == "/" and num2 > 0 and num2 < 0:
    print(num1 / num2)
else:
    print("datos no validos")

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

año = int(input("Coloque un año \n"))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("Es año biciesto")
else:
    print("No es año biciesto")

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

age = int(input("introduce una edad"))

if age >= 0 and age <= 2:
    print("Bebe")
elif age >= 3 and age <= 12:
    print("Niño")
elif age >= 13 and age <= 17:
    print("Adolecente")
elif age >= 18 and age <= 64:
    print("Adulto")
elif age > 65:
    print("Adulto mayor")
else:
    print("dato invalido")