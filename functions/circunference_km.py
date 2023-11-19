
import math


def circunference_km(raio_km):
    """
    calcula a circunferência conforme o raio informado
    o objetivo é abstrair o tamanho do caminho que precisa ser preenchido 
    portanto a essa função representa o tamanho do caminho

    :param kmh: Km por hora.
    """
   
    return math.pi * (raio_km * 2)
