def valores_al_cuadrado(lista_numeros):
    """
    Calcula los valores al cuadrado de una lista de números.

    Parámetros:
    lista_numeros (list): Una lista de números.

    Retorna:
    list: Una lista con los valores al cuadrado de los números en la lista.
    """
    return [numero ** 2 for numero in lista_numeros]

# Ejemplo de uso:
numeros = [2, 4, 6, 8, 10]
valores_cuadrado = valores_al_cuadrado(numeros)
print(f"Valores al cuadrado de la lista {numeros}: {valores_cuadrado}")
