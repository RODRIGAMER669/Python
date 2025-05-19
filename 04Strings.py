## Strings

my_string = "Mi string"
mi_otro_string = "Mi  otro string"

print(len(my_string))
print(len(mi_otro_string))

print(my_string + " "+ mi_otro_string)

mi_nueva_linea_string = "Este es un String \ncon salto de línea"
print(mi_nueva_linea_string)

mi_tabulacion_string = "\tEste es un String con salto de línea"
print(mi_tabulacion_string)

mi_escape_string = "\\tEste es un String \\nescapado" # Ignora las tabulaciones, saltos de línea
print(mi_escape_string)

# Formateo

name, surname, edad = "Alexis", "Rodríguez", 35

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, edad))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, edad))
print(f"Mi nombre es {name} {surname} y mi edad es {edad}")

## Desempaquetado de caracteres
language = "python"
a, b, c, d, e, f = language
print(a)
print(f)

## División

separar_palabra = language[1:3]
print(separar_palabra)

separar_palabra = language[1:]
print(separar_palabra)

separar_palabra = language[0:6:2]
print(separar_palabra)

## Reverse

reversed_lenguage = language[::-1]
print(reversed_lenguage)

# Funciones

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.lower().isupper())
print(language.startswith("py"))
print(language.lower())
