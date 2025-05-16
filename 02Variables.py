# Variables

mi_variable = 'Mi variable String'
print(mi_variable)

mi_int_variable = 5
print(mi_int_variable)

mi_int_to_str = str(mi_int_variable) # Transforma el tipo numero a str
print(mi_int_to_str)
print(type(mi_int_to_str))

mi_bool_variable = True
print(mi_bool_variable)

# Concatenar cadenas
print(mi_variable, str(mi_int_variable), mi_bool_variable)
print("El valor de mi_bool_variable es", mi_bool_variable)

# Funciones del sistema
print(len(mi_variable))

# Variables en una sola linea
nombre, apellido, edad = "Alexis", "Rodríguez", 19
print(nombre, apellido, edad)

# Inputs
nombre = input('Cuál es tu nombre?')
anho = input("Cuales tu edad")
 
print(nombre)
print(anho)

# Cambiamos tipos
name = 35
age = "patata"
print(name)
print(anho)

# Forzamos el tipo
address: str = "Mi dirección"
address: int = 32
print(type(address))