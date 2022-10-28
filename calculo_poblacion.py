from shapely.geometry import Point, Polygon, mapping
import matplotlib.pyplot as plt
import argparse
import glob
import os
import pandas as pd
import geopandas as gpd
from shapely import wkt
import openpyxl
import os


parser = argparse.ArgumentParser(description='Calcula la extension territorial y poblacion total de un grupo de coberturas .shp dentro del territorio nacional')
# Optional positional argument
parser.add_argument('--folder', type=str,
                    help='Nombre de la carpeta que contiene los poligonos .shp',  default='./datos/coberturas/')

# Required argument
parser.add_argument('--nombre_destino', type=str,
                    help='Nombre de los archivos que se generaran: Todos los archivos resultado tendran este nombre como prefijo', required= True)

# Switch
parser.add_argument('--map', action='store_true',
                    help='Si se parsea este argumento, se generará un mapa con los resultados')

args = parser.parse_args()

#Importamos los puntos de poblacion
inegi_path='./Localidades_20100_semicolon.csv'
inegi_data = pd.read_csv(inegi_path,header=0, delimiter = ";", encoding = 'latin-1')
#Importamos los shp de cobertura

coberturas_dir = args.folder #Local path, you can change it to mkae it matc your files route. i.e. '/csv/' , '../../Documents/"
coberturas_dir_list = glob.glob(os.path.join(coberturas_dir, '*.shp'))
print("Archivos de cobertura incluidos: ", len(coberturas_dir_list))


# datos para almacenar resultados
folder_name = './results/' + args.nombre_destino + '/'
if not os.path.exists(folder_name):
   os.makedirs(folder_name)
   
dataset_filename = folder_name + args.nombre_destino + '_dataset.xlsx'
shp_filename =  folder_name + args.nombre_destino + '_localidades.shp'
report_filename = folder_name + args.nombre_destino + 'report.csv'


gdf_base = gpd.GeoDataFrame(
    inegi_data, geometry=gpd.points_from_xy(inegi_data.LONGITUD, inegi_data.LATITUD))

gdf_base.set_crs(epsg=4326, inplace=True)

localidades_incluidas = set()

for cobertura in coberturas_dir_list:
    cobertura_shp= gpd.read_file(cobertura)
    points_within = gpd.sjoin(gdf_base,cobertura_shp, predicate='within')
    print("Procesada estacion: ", cobertura)
    
    localidades_incluidas.update(points_within["_ID"].to_list())
    
# print(localidades_incluidas)
print(len(localidades_incluidas), " Localidades incluidas en el grupo ", args.nombre_destino)
localidades_incluidas_df = pd.DataFrame(list(localidades_incluidas),columns = ['_ID']) 

result_coverage = pd.merge(localidades_incluidas_df,inegi_data, on='_ID', how='left')
print(result_coverage)

writer = pd.ExcelWriter((dataset_filename),engine='openpyxl')
result_coverage.to_excel(writer,index = True, header=True)
writer.save()

# Geopandas GeoDataFrame
result_coverage_shp = gpd.GeoDataFrame(result_coverage, geometry='geometry')
#Export to shapefile
result_coverage_shp.to_file(shp_filename)

extension_territorial =  result_coverage['SUPERFICIE'].sum(axis=0)
print("Extension territorial de las localidades incluidas: ", extension_territorial, " km^2")

results = {'Nombre del grupo: ': args.nombre_destino,'Numero de localidades: ': len(coberturas_dir_list),'Extensión territorial: ':extension_territorial}
##Guardamos resultados
def write_results():
    with open(report_filename, 'w') as f:
        for key in results.keys():
            f.write("%s, %s\n" % (key, results[key]))
            
write_results()
print ('Listo')