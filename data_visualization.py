from bokeh.plotting import figure, save
from bokeh.models import ColumnDataSource

import pandas as pd
import geopandas as gpd

p = figure(title="Mapa de cobertura")
print(p)

base_map = r"./datos/datasets/INEGI_2010/estatal.shp"
population_dots = r"./results/result.shp"

points_gdf = gpd.read_file(population_dots)
base_map_gdf = gpd.read_file(base_map)
print(points_gdf.head)

points_to_plot_source = pd.dataframe()

psource = ColumnDataSource(points_gdf)

# Initialize our plot figure
p = figure(title="A map of Localidades dentro de la estacion")

# Add the points to the map from our 'psource' ColumnDataSource -object
p.circle('LONGITUD', 'LATITUD', source=psource, color='red', size=10)

# Output filepath
outfp = r"./maps/map01.html"

# Save the map
save(p, outfp)

# outmap_route = r"./maps/map01.html"
# save(obj=p, filename=outmap_route)

  