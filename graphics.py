import pandas as pd
import matplotlib.pyplot as plt
from analysis import *

# Graphic of the total sales per decade.

def visualize(df):
    title= '90s the gold decade of Video Games'
    Data = {'Decade': ["80's","90's","2000"],
            'Sales in milions': [40.24,31.37,82.53]       
        }
    
    cd = pd.DataFrame(Data,columns=['Decade','Sales in milions'])
    cd.plot(x ='Decade', y='Sales in milions', kind = 'line')
    
    return plt.show()

