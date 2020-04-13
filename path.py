import pandas as pd

def acquire():
  df = pd.read_csv('../../csv/Nintendo_Sales.csv')
  if isinstance(df, pd.DataFrame): 
    return df
  if not isinstance(df, pd.DataFrame): 
    print('NO instancia')
    raise Exception("Error al obtener los datos.")