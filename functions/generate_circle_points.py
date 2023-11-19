import math
from functions.circunference_km import circunference_km
from functions.km_per_second import km_per_second

def generate_circle_points(lat, lon, speed, detect_second=4, radius=10000):
    """
    Gera pontos de latitude e longitude em um círculo de raio definido em torno de um ponto central.
    essa função usa a circuferencia (caminho) e o km/segundo (tamanho do passo) calcula o radio e plota os pontos

    :param lat: Latitude do ponto central em graus. 
    :param lon: Longitude do ponto central em graus.
    :param speed: Velocidade em km por hora.
    :param detect_second: ciclo em segundos de detecção do radar (Padrão 4 segundos)
    :param radius: Raio do círculo em metros (padrão 5km).
    :return: Lista de tuplas contendo as coordenadas (latitude, longitude) dos pontos gerados.
    """


    # Quantidade de ponto no tempo
    
    circuference    = circunference_km(radius)
    kmSec           = km_per_second(speed,detect_second)
    
    if kmSec > circuference:
        print("geometria impossivel, velocidade maior que a distancia a percorrer")
        exit()

    num_points = int(circunference_km(radius) / km_per_second(speed,detect_second))

    # Conversão das coordenadas do ponto central para radianos
    lat_rad = math.radians(lat)
    lon_rad = math.radians(lon)

    # Raio da Terra
    earth_radius = 6371000

    #plotando...
    points = []
    for i in range(num_points):
        # Calculando o ângulo (em radianos) para cada ponto
        angle = 2 * math.pi * i / num_points

        # Novas coordenadas em radianos
        new_lat_rad = math.asin(math.sin(lat_rad) * math.cos(radius / earth_radius) +
                                math.cos(lat_rad) * math.sin(radius / earth_radius) * math.cos(angle))
        new_lon_rad = lon_rad + math.atan2(math.sin(angle) * math.sin(radius / earth_radius) * math.cos(lat_rad),
                                           math.cos(radius / earth_radius) - math.sin(lat_rad) * math.sin(new_lat_rad))

        # Convertendo as novas coordenadas para graus
        new_lat = math.degrees(new_lat_rad)
        new_lon = math.degrees(new_lon_rad)

        points.append((new_lon, new_lat))

    return points
