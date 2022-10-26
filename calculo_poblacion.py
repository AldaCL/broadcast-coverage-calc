from shapely.geometry import Point, Polygon, mapping
import argparse
import glob
import os
import pandas as pd
import geopandas as gpd


parser = argparse.ArgumentParser(description='Calcula la extension territorial y poblacion total de un grupo de coberturas .shp dentro del territorio nacional')
# Required positional argument
parser.add_argument('--folder', type=str,
                    help='Nombre de la carpeta que contiene los poligonos .shp',  default='./datos/coberturas/')

# Optional argument
parser.add_argument('--nombre_destino', type=str,
                    help='Nombre de los archivos que se generaran: Todos los archivos resultado tendran este nombre como prefijo', required= True)

# Switch
parser.add_argument('--map', action='store_true',
                    help='Si se parsea este argumento, se generará un mapa con los resultados')

args = parser.parse_args()

#importamos los puntos de poblacion
inegi_path='./Localidades_20100_semicolon.csv'
inegi_data = pd.read_csv(inegi_path,header=0, delimiter = ";", encoding = 'latin-1')
#Importamos los shp de cobertura

coberturas_dir = args.folder #Local path, you can change it to mkae it matc your files route. i.e. '/csv/' , '../../Documents/"
coberturas_dir_list = glob.glob(os.path.join(coberturas_dir, '*.shp'))
print("Archivos de cobertura incluidos: ", len(coberturas_dir_list))

gdf_base = gpd.GeoDataFrame(
    inegi_data, geometry=gpd.points_from_xy(inegi_data.LONGITUD, inegi_data.LATITUD))

gdf_base.set_crs(epsg=4326, inplace=True)

localidades_incluidas = []

localidades_incluidas_series = pd.Series

print(args.nombre_destino)

for cobertura in coberturas_dir_list:
    cobertura_shp= gpd.read_file(cobertura)
    points_within = gpd.sjoin(gdf_base,cobertura_shp, predicate='within')
    print("Procesada estacion: ", cobertura)
    
    localidades_incluidas_series.concat(points_within['_ID'])
    
    # for i in points_within.index:
    #     localidades_incluidas.append(points_within["_ID"][i])
    
localidades_incluidas_series = localidades_incluidas_series.unique()
# resultado = set(localidades_incluidas)
print(localidades_incluidas_series)
print(localidades_incluidas_series.shape)
# cobertura_1 = gpd.read_file(coberturas_dir_list[0])

# print(gdf.head())
# print(gdf.shape)
# print(cobertura_1)


# print(points_within)
# print(points_within.shape)

# points_within.to_file('./results/map01.shp')
