import math

def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo.

    Parámetros:
    radio (float o int): Radio del círculo.

    Retorna:
    float: El área del círculo.
    """
    if radio < 0:
        return None
    area = math.pi * (radio ** 2)
    return area


def calcular_volumen_cilindro(radio, altura):
    """
    Calcula el volumen de un cilindro utilizando el área del círculo.

    Parámetros:
    radio (float o int): Radio de la base del cilindro.
    altura (float o int): Altura del cilindro.

    Retorna:
    float: El volumen del cilindro.
    """
    if radio < 0 or altura < 0:
        return None
    area_base = calcular_area_circulo(radio)
    volumen = area_base * altura
    return volumen



