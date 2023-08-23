def sumar_con_kwargs(**kwargs):
    resultado = 0
    for key, value in kwargs.items():
        resultado += value
    return resultado


'''
NOTA Acerca de **kwargs

En **kwargs se recibe un número indeterminado de argumentos desde cualquier
variable de tipo dict
'''
numeros = {"numero1": 10, "numero2": 20, "numero3": 30}
resultado = sumar_con_kwargs(**numeros)
print(f"La suma de los números es: {resultado}")
