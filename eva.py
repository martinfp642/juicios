import csv
import openpyxl
import random
from openpyxl import Workbook


def cargar_juicios_desde_csv():
    juicios = {}
    with open("juicios.csv", "r", encoding="utf-8") as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            if len(row) < 2:
                continue  # Saltar filas que no tengan al menos dos elementos
            nota = int(row[0])
            juicio = row[1]
            if nota not in juicios:
                juicios[nota] = []
            juicios[nota].append(juicio)
    return juicios


def juicio_evaluacion(nota, juicios):
    nota_entera = int(nota)
    while nota_entera >= 1:
        if nota_entera in juicios:
            return random.choice(juicios[nota_entera])
        nota_entera -= 1
    return "Sin juicio disponible"


def procesar_notas(archivo_entrada, archivo_salida, juicios):
    # Leer archivo de entrada
    with open(archivo_entrada, "r", encoding="utf-8") as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)  # Saltar encabezado

        # Crear archivo de salida
        wb = Workbook()
        ws = wb.active
        ws.append(["Nombre", "Apellido", "Nota", "Juicio"])

        for row in csv_reader:
            nombre, apellido, nota = row[0], row[1], float(row[2])
            juicio = juicio_evaluacion(nota, juicios)

            ws.append([nombre, apellido, nota, juicio])

    wb.save(archivo_salida)


if __name__ == "__main__":
    archivo_entrada = "estudiantes.csv"
    archivo_salida = archivo_entrada.split(".")[0] + "_promedios.xlsx"

    juicios_dict = cargar_juicios_desde_csv()
    procesar_notas(archivo_entrada, archivo_salida, juicios_dict)
    print(f"Archivo de salida generado: {archivo_salida}")

