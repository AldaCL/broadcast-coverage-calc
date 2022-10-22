from shapely.geometry import Point, Polygon, mapping
import csv 
import glob
import os
import pandas as pd
import geopandas as gpd
import fiona


#importamos los puntos de poblacion
inegi_path='./Localidades_20100_semicolon.csv'
inegi_data = pd.read_csv(inegi_path,header=0, delimiter = ";", encoding = 'latin-1')
#Importamos los shp de cobertura

coberturas_dir = './Datos/FM/' #Local path, you can change it to mkae it matc your files route. i.e. '/csv/' , '../../Documents/"
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


# coords = [(24.950899, 60.169158), (24.953492, 60.169158), (24.953510, 60.170104), (24.950958, 60.169990)]
# poly = Polygon(coords)
# cobertura_1 = gpd.read_file(coberturas_dir_list[0])

# shape = fiona.open(coberturas_dir[0])
# print (shape.schema)
# # {'geometry': 'LineString', 'properties': OrderedDict([(u'FID', 'float:11')])}
# #first feature of the shapefile
# first = shape.next()
# print (first) # (GeoJSON format)

# print(p3.within(cobertura_1))