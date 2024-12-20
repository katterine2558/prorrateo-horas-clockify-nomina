import pandas as pd

#LEE LA BASE DE DATOS DE LOS EMPLEADOS
def read_database():

    #Lee la base de datos de los colaboradores
    df = pd.read_excel("G:/Unidades compartidas/BD Administración/01. BD_COLABORADORES/BD COLABORADORES.xlsx",index_col=None,header=0)
    df = df[~df['SEDE'].isin(['CDMX', 'Lima'])]

    #Inicializa el diccionario para almacenar
    employees = {
    "No.": [],
    "IDENTIFICACIÓN": [],
    "NOMBRE": [],
    "CORREOS": []
    }

    #Columna de identificación
    for value in df["IDENTIFICACIÓN"].to_list():
        if value != '':
            try:
                employees["IDENTIFICACIÓN"].append(int(value))
            except:
                employees["IDENTIFICACIÓN"].append(int(value.split("CE ")[1]))

    #Columna de nombre
    for value in df["NOMBRE"].to_list():
        if value != '':
            employees["NOMBRE"].append(value)
            

    #Columna de correos
    for value in df["CORREO"].to_list():
        if value != '':
            employees["CORREOS"].append(value.strip())  

    #Columna de número de identificación
    i=1
    for _ in range(len(employees["IDENTIFICACIÓN"])):
        employees["No."].append(i)
        i+=1

    return employees