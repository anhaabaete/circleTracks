
def km_per_second(kmh, detect_second):
    """
    calcula km hora por distancia em segundo
    o objetivo é abtrair o calculo do ciclo de passos
    pois cada km/second é um passo, então a função é 'o tamanho do passo'

    :param kmh: Km por hora.
    :param detect_second: ciclo por segundo.
    """
    
    return ((kmh / 3600) * detect_second) * 1000 # vezes 1000 para KM
