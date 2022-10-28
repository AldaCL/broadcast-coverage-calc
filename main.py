import calculo_poblacion,data_visualization
import argparse
import os


def main():
    args = argumen_parser()
    folder_name = './results/' + args.nombre_destino + '/'
    
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        
    dataset_filename = folder_name + args.nombre_destino + '_dataset.xlsx'
    shp_filename =  folder_name + args.nombre_destino + '_localidades.shp'
    report_filename = folder_name + args.nombre_destino + 'report.csv'

    calculo_poblacion.run(args,dataset_filename,shp_filename,report_filename)
    
    if args.map :
        data_visualization.generate()
    else:
        pass

def argumen_parser():
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
    
    return args
    

if __name__ == '__main__':
    main()