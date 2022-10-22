from shapely.geometry import Point, Polygon, mapping
import csv 
import glob
import os
import pandas as pd
import geopandas as gpd

#importamos los puntos de poblacion
inegi_path='./Localidades_20100_semicolon.csv'
inegi_data = pd.read_csv(inegi_path,header=0, delimiter = ";", encoding = 'latin-1')
#Importamos los shp de cobertura

coberturas_dir = './datos/FM/' #Local path, you can change it to mkae it matc your files route. i.e. '/csv/' , '../../Documents/"
coberturas_dir_list = glob.glob(os.path.join(coberturas_dir, '*.shp'))
print(coberturas_dir_list)

gdf = gpd.GeoDataFrame(
    inegi_data, geometry=gpd.points_from_xy(inegi_data.LONGITUD, inegi_data.LATITUD))

gdf.set_crs(epsg=4326, inplace=True)

cobertura_1 = gpd.read_file(coberturas_dir_list[0])

print(gdf.head())
print(gdf.shape)
print(cobertura_1)

points_within = gpd.sjoin(gdf,cobertura_1, predicate='within')

print(points_within)
print(points_within.shape)

points_within.to_file('./results/map01.shp')
