import pandas as pd
import matplotlib
import sys
import os
import matplotlib.pyplot as plt
import GrapApi

outPath= 'output/'

def acquire(filePath):
  df = pd.read_csv(filePath)
  if isinstance(df, pd.DataFrame): 
    return df
  if not isinstance(df, pd.DataFrame): 
    print('NO instancia')
    raise Exception("Error al obtener los datos.")

def Global_Sales(df):
  df_selected = df[['Global_Sales','Genre', 'Year_of_Release','Developer','Name','JP_Sales','EU_Sales','NA_Sales']]
  
  df_selected = df_selected[df_selected['Global_Sales'] >= 25] 
  df_selected.loc[df_selected.Developer.isnull(), "Developer"] = ["Nintendo"]

  df_selected["Year_of_Release"] = df_selected.Year_of_Release.astype(int)
  df_selected['Global_Sales'].sum()
  return df_selected

def Sales_Decade(df):
  df_selected["decada"] = pd.cut(df_selected.Year_of_Release,
                                bins=[1979,1989,1999,2009,2019], 
                                 labels=range(1980,2020,10))
  df_Decada=df_selected.groupby('decada').agg(({"Global_Sales":["mean","max","min"]}))
  
  return df_Decada

def Data(df, name):
  serie = df[name].value_counts().sort_index()
  return serie

def visualize(name, df= None, ser= None):
  print('\n-------------{}-------------'.format(name))
  if df is not None: print(df.to_string())
  elif ser is not None: print(ser.to_string())

def save_plots(name, df= None, ser= None, x= None, y= None, tipo='bar'):
  plt.figure(figsize=(12,8))
  if df is not None: 
    df.plot(x, y, color='red', kind=tipo, figsize=(12,8)) 
  elif ser is not None: 
    ser.plot(kind=tipo)

  plt.title(name)
  save_path= os.path.join(outPath,name+'.png')
  plt.savefig(save_path)


#Ejecución del programa principal
def ejecutar(filePath):
  try:
    df = acquire(filePath)
    print('Getting Nintendos data...')
  except Exception:
    print('Check path to get csv file')
    sys.exit(-1)
    
  df_selected= Global_Sales(df)
  df_selected= Sales_Decade(df_selected)

  # Estudio de categorías de puntuación.
  categories_serie= data(df_selected, 'category')
  visualize('data from ', ser=data)
  save_plots('data from', ser=data)


  #Top ten populares
  df_api= igdbApi()
  visualize('Top 10 popular today', df_api)
  save_plots('top10 popular today', df=df_api.sort_values('popularity'), x= 'name', y='popularity', tipo='barh')