def sumar_con_args(*args):
    resultado = 0
    for num in args:
        resultado += num
    return resultado


numeros = 1, 2, 3, 4, 5
resultado = sumar_con_args(*numeros)
print(f"La suma de los números es: {resultado}")
