# Ejercicio 5: Multiplicación de dos números ingresados por consola.

# Descripción:
# En este ejercicio utilizaremos la captura de datos con la ayuda del "input". Recuerda definir las variables de entrada y la que posteriormente recibir el resultado de la operación.

# 1. Definir variables de los números que le vas a solicitar al usuario, ya sean de tipo entero o flotante. Recuerda utilizar el input para el ingreso de datos.

num_1= int(input("Ingresa un número :"))
num_2= int(input("Ingresa otro número :"))



# 2. Definir la variable que recibirá el resultado de la multiplicación y en la cual se hará la operación.

resultado = num_1*num_2

# 3. Ejecute el programa. Recuerda imprimir el resultado en la consola.

print(f"La multiplicación de {num_1} x {num_2} es {resultado}")

#Tip: Recuerda que al capturar los datos en el inicio, debes envolver ambos inputs con int* puesto que el programa los leerá como si fueran strings y no se ejecutará la operación matemática. 




