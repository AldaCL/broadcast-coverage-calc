# Puntos sobre polígonos con GeoPandas y Bokeh🌎

Este proyecto simplifica y automatiza el cálculo de puntos incluidos dentro de poligonos (point-in-polygon (PIP) problem), en el contexto de datos georreferenciados , utilizando GeoPandas y Bokeh para la visualización en un mapa de México

## Detalle
Este programa tiene por objetivo automatizar y simplificar el cálculo de "Puntos que se encuentran sobre uno o varios polígonos". Utilizando un grupo de archivos _**.shp**_ que representan los polígonos de interés, así como un archivo **base** de puntos dados por coordenadas X Y que postreriormente fueron covertidos a geometrías de puntos georeferenciados (Points).

El código base no solo permite identificar y extraer los puntos que se encuentran dentro del grupo de polígonos dado, sino devolver algunos datos clave como el total de superficie que representan las poblaciones incluidas, o la distribución de población por edad, sexo, etc ... dependiendo de los datos contenidos dentro de las capas (CSV o .shp)

## Instalación

El código base se desarrollo con Python 3.8, por lo que se recomienda generar un entorno virtual con esta versión de Pyhthon. Para lograr esto, se requiere tener instalada una versión de Python igual o superior a la 3.8, a continuación:

1. Asegurese de tener instalado venv:

    `pip install virtualenv`

2. Genere un nuevo entorno virtual, cambia "name" por el nombre de tu elección:

    `python -m virtualenv_name --python = python3.8`

3. Inicie el nuevo virtual env:

    `source virtualenv_name/bin/activate`

4. Instale los paquetes listados en el archivo **requirements.txt**

    `pip install -r requeriments.txt`

5. Deberá colocar un par de ficheros necesarios: 

- **Datos requeridos**

	 - Polígonos *.shp* de capa de estados de la República Mexicana, **INEGI**, 2010: [Descarga](https://www.inegi.org.mx/app/biblioteca/ficha.html?upc=702825296520) (datos/datasets/INEGI_2010/estatal.shp)
	 - Lista de Localidades de México, **INEGI**, 2010: [Descarga](https://www.inegi.org.mx/contenidos/programas/ccpv/2010/datosabiertos/iter_nal_2010_csv.zip ) (Localidades_20100_semicolon.csv)
	- Coberturas de radiodifusión **IFT**:  [Consulta CPCREL](http://mapasradiodifusion.ift.org.mx/CPCREL-web/consultaCoberturas/consultaCoberturas.xhtml;jsessionid=U-8eUGaEZNAYqrD8aTpGOYH0vn-6YGkZmI6KeQozd527haXDVzNQ!271094803?dswid=6870) (**polígonos a colocar en el fichero datos/coberturas**, pueden descargarse en formatos kmz y podría ser transformado a shp)
	
## Manual de uso 

Es posible ejecutar el programa principal `main.py` con el entorno virtual activado, y esta ejecución podrá tomar los siguientes argumentos:

- `--nombre_destino`: Nombre de la carpeta y ficheros con los que se identificaran los archivos resultado. (Obligatorio)
- `--folder`: Ruta de la carpeta que contiene los polígonos, por defecto es /*datos/coberturas/*
- `--map`: Incluir esta bandera generará adicionalmente un mapa interactivo con Bokeh para tener una visualización de datos sin necesidad de cargar los polígonos .shp en algún software de GIS.


Así, por ejemplo, una vez colocados los archivos necesarios, es posible ejecutar:

`python main.py --nombre-destino TEST1 --map`

Lo cual generará 3 archivos principales como resultado en los folders **maps/TEST1** y **results/TEST1**

- ***TEST1.shp*** contiene los puntos que se encontraron dentro del grupo de polígonos encontrados en **datos/coberturas**.

- ***TEST1_dataset.xlsx*** Contiene los datos del geodataframe de los puntos dentro del polígono, con el objetivo de mantener los datos adicionales de cada capa.

- ***TEST1_report.csv*** Contiene un reporte de los campos de los layers (Puede modificarse que campos se requieren), por defecto únicamente reporta la cantidad de polígonos utilizados en el cálculo y la extensión territorial que se encuentra en el campo *SUPERFICIE* en km^2 

- ***maps/TEST1.html*** Dónde vive la visutalización de datos en el mapa base de la républica Mexicana, realizada con Bokeh.



If you get any issues feel free of contact me at: aldair.alda27@gmail.com