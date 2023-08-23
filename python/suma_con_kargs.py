def sumar_con_kwargs(**kwargs):
    resultado = 0
    for key, value in kwargs.items():
        resultado += value
    return resultado


numeros = {"numero1": 10, "numero2": 20, "numero3": 30}
resultado = sumar_con_kwargs(**numeros)
print(f"La suma de los números es: {resultado}")
