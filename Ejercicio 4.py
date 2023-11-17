def calcular_media(lista_numeros):
    """
    Calcula la media de una lista de números.

    Parámetros:
    lista_numeros (list): Una lista de números.

    Retorna:
    float: La media de los números en la lista.
    """
    if not lista_numeros:
        return 0  # Devolver 0 si la lista está vacía para evitar errores de división por cero
    suma = sum(lista_numeros)
    media = suma / len(lista_numeros)
    return media
numeros = [2, 4, 6, 8, 10]
resultado = calcular_media(numeros)
print(f"La media de la lista {numeros} es: {resultado}")