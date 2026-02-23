# Ejercicio 06: Control de acceso a usuario con operadores lógicos y datos de tipo booleano.

# Descripción:
# En este ejercicio vamos a emplear los datos de tipo booleanos y para ello, será importante aplicar estructuras de ciclos. 

# 1. Defina las variables que permitirán el acceso correcto del programa.

usuario_sistema= "Emily"
contrasena_sistema =123456

# 2. Estructure la captura de datos acorde a las variables definidas anteriormente. Recuerde que es imprescindible el uso del "input".

usuario= input("Ingrese el usuario: ")
contrasena= int (input("Ingrese la contraseña: "))

# 3. Defina la estructura de ciclos de acuerdo a las condiciones que permitan el correcto uso de las variables para acceder con éxito en el programa. 
if usuario_sistema == usuario and contrasena_sistema == contrasena:
    print("Bienvenido al sistema")

else:
    print("Acceso denegado. Intente de nuevo.")

# 4. Ejecute el programa.

# Tip: Recuerde que en Python, el operador lógico && = "and".
