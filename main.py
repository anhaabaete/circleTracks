import math
import geojson

from functions.generate_circle_points import generate_circle_points
from functions.splot_geojson import splot_geojson


# Lat long Sao paulo
lat_ref = -23.5489  # Latitude de referência
lon_ref = -46.6388  # Longitude de :param kmh: Km por hora.


# Gerando os pontos
circle_points = generate_circle_points(lat_ref, lon_ref, 900)


# Coordenadas
geojson = splot_geojson(circle_points)




print(geojson)