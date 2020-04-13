import pandas as pd

 
def Sales(df,decade,country):
    df['decade'] == decade
    df=df.groupby('decade').agg(({country:['max']}))
    df_final=df.sum()
    
    return  f'The total sales on {decade} was: {df_final[0]}% of the total sales.'