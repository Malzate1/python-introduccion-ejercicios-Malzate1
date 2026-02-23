
# Ejercicio 3: Suma de enteros de un set.

# Descripción:
# En este ejercicio desarrollarás el uso de la suma sin ejecutar el operador "+". Gracias a la parabra reservada "sum", podrás ejecutar la operación.

# 1. Define un set de numeros enteros.

set_impar = {3,5,7,17,19}

# 2. Define la variable que recibirá el total para aplicar la suma. Recuerda utilizar un bucle "for" para realizar la suma.
suma=0

for numero in set_impar:
    suma +=numero


# 3. Imprime el resultado utilizando print().

print(f"La suma del set impar es  {suma}")

# 4. Ejecuta el programa.

#Tip: Recuerda emplear la interpolación en la impresión: (print(f""))


