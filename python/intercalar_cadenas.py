def intercalar_mayusculas_minusculas(cadena):
    resultado = ""
    mayusculas = True

    for letra in cadena:
        if mayusculas:
            resultado += letra.upper()
        else:
            resultado += letra.lower()

        # Cambiar el valor de 'mayusculas' para la siguiente iteración
        mayusculas = not mayusculas

    return resultado


# Pedir al usuario que ingrese una cadena
entrada = input("Ingresa una cadena: ")

# Llamar a la función y mostrar el resultado
resultado_intercalado = intercalar_mayusculas_minusculas(entrada)
print("Cadena intercalada:", resultado_intercalado)
