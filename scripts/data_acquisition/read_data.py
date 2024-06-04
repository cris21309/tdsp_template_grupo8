import pandas as pd

print('¡Hola! Bienvenido al sistema de detección de diabetes.\n')

def registro(dir):
    df=pd.read_csv(dir)
    return df

print('Ingresa una tabla de datos en formato csv: \n')
df = registro(str(input()))

n_registros = int(input("¿Cuantos registros quieres cargar?: \n"))

df = df[:n_registros]

print(f'Cantidad de registros cargados con exito: {df.shape[0]}')
