def sumar_con_args(*args):
    resultado = 0
    for num in args:
        resultado += num
    return resultado


'''
NOTA Acerca de *args

En *args se recibe un número indeterminado de argumentos desde cualquier
variable de tipo list o tuple
'''
numeros = 1, 2, 3, 4, 5
resultado = sumar_con_args(*numeros)
print(f"La suma de los números es: {resultado}")
