import csv

def extraer_info_notas(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'r', encoding='ISO-8859-1') as notas_csv:
        csv_reader = csv.reader(notas_csv)
        header = next(csv_reader)
        
        with open(archivo_salida, 'w', encoding='UTF-8', newline='') as estudiantes_csv:
            csv_writer = csv.writer(estudiantes_csv)
            csv_writer.writerow(["Nombre", "Apellido", "Nota"])
            
            for row in csv_reader:
                first_name = row[0]
                last_name = row[1]
                promedio_general = row[3]
                csv_writer.writerow([first_name, last_name, promedio_general])

extraer_info_notas("notas.csv", "estudiantes.csv")

