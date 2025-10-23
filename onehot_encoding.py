import pandas as pd
import numpy as np

df=pd.read_csv("train.csv")

def onehot_encoder(df,column_name):
    df = df.copy()
    for val in df[column_name].dropna().unique():
        df[val] = (df[column_name] == val).astype(int)

    return df
        
    

print(onehot_encoder(df,"SaleCondition"))