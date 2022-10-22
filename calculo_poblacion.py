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
    inegi_data, geometry=gpd.points_from_xy(inegi_data.LATITUD, inegi_data.LONGITUD))

# Create Point objects
p1 = Point(24.952242, 60.1696017)
p2 = Point(24.976567, 60.1612500)
p3 = Point(inegi_data.LATITUD[1], inegi_data.LONGITUD[1])

# Create a Polygon
coords = [(24.950899, 60.169158), (24.953492, 60.169158), (24.953510, 60.170104), (24.950958, 60.169990)]
poly = Polygon(coords)
cobertura_1 = gpd.read_file(coberturas_dir_list[0])

schema = {
    'geometry': 'Polygon',
    'properties': {'id': 'int'},
}

# Write a new Shapefile
with fiona.open(coberturas_dir_list[0], 'w', 'ESRI Shapefile', schema) as c:
    ## If there are multiple geometries, put the "for" loop here
    c.write({
        'geometry': mapping(poly),
        'properties': {'id': 123},
    })
print(cobertura_1)


print(p3.within(cobertura_1))