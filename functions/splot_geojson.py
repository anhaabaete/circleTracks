import geojson


#organiza todo em uma coleção GeoJSON
def splot_geojson(coordinates):

    # Criar uma lista de features de pontos
    point_features = []
    for coordinate in coordinates:
        point = geojson.Point(coordinate)
        feature = geojson.Feature(geometry=point, properties={})
        point_features.append(feature)

    # Criar uma coleção de features
    feature_collection = geojson.FeatureCollection(point_features)

    # Serializar para JSON
    geojson_str = geojson.dumps(feature_collection, sort_keys=True)

    # Imprimir o GeoJSON resultante
    return geojson_str