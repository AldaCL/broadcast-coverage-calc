from email.mime import base
from bokeh.plotting import figure, save
from bokeh.models import ColumnDataSource, GeoJSONDataSource

import pandas as pd
import geopandas as gpd

base_map = r"./datos/datasets/INEGI_2010/estatal.shp"
population_dots = r"./results/map01.shp"

points_gdf = gpd.read_file(population_dots)
print(points_gdf.head)

base_map_gdf = gpd.read_file(base_map)
base_map_gdf.set_crs(epsg=6362, inplace=True)
print(base_map_gdf.crs)

base_map_gdf_correction = base_map_gdf.to_crs({'init': 'epsg:4326'})
print(base_map_gdf_correction)


points_to_plot_source = points_gdf[['LONGITUD','LATITUD']]
print(points_to_plot_source)

base_map_source = GeoJSONDataSource(geojson=base_map_gdf_correction.to_json())


p = figure(title="Mapa de cobertura",plot_height = 700 ,
           plot_width = 1000,output_backend="webgl")
print(p)


p.multi_line('xs', 'ys', source=base_map_source, color='gray',
                   line_color = 'gray', 
                   line_width = 2)

psource = ColumnDataSource(points_to_plot_source)
# Initialize our plot figure
# Add the points to the map from our 'psource' ColumnDataSource -object
p.circle('LONGITUD', 'LATITUD', source=psource, color='red', size=3)

outmap_route = r"./maps/map02.html"
save(obj=p, filename=outmap_route, title='Localidades dentro de Cobertura')

  