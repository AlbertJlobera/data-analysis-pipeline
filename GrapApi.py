import json
import requests
import os
import pandas as pd
from dotenv import load_dotenv
load_dotenv()

def UseApi():
    IGDB_TOKEN = os.getenv("IGDB_TOKEN")
    key = IGDB_TOKEN
    url = 'https://api-v3.igdb.com/games/'
    body= 'fields name,popularity; sort popularity desc;'
    response = requests.post(
    url,
    data= body,
    headers={'user-key': key,
              'Content-Type': 'application/json; charset=UTF-8'
            }
    )

    result = response.json()
    df_api = pd.DataFrame(result)
    return df_api

df_api= UseApi()