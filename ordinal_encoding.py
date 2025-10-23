import pandas as pd
import numpy as np

df=pd.read_csv("train.csv")

def ordinalencoder(df,column_name):
    df=df.copy()
    # distinct_values=set(df[column_name])
    c=0
    d={}
    

    for i in df[column_name].dropna().unique():
        d[i]=c
        c+=1
    

    df[column_name]=df[column_name].map(d)
    return df
    

df=ordinalencoder(df,"SaleCondition")
print(df["SaleCondition"].unique())
