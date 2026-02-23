# Ejercicio 08: Verificador de números pares-impares.

# Descripción : Con la ayuda de condicionales, aplicaremos el uso del operador módulo e identificar si un número es par o impar. Debemos implementar el ingreso de datos del usuario para aplicar el funcionamiento del script construido.

# 1. Define la variable de captura. Recuerda implementar el "input" para iniciar el uso de la consola.

# 2. Utiliza la estructura de condicionales y el operador módulo para definir el ciclo que evaluará el número que introduzca el usuario y finalmente se pueda realizar la verificación del mismo.

# 3. Ejecuta el programa.

# Tips: Recuerda que el operador módulo (%) se utiliza para obtener el residuo en una división.
#       No olvides convertir la variable de entrada para que no haya errores al ejecutar el script.


num=int(input("Introduce un número entero: "))

if num % 2 == 0:
    print(f"El {num} es un número par")

else :
    print(f"El {num} es un número impar")

