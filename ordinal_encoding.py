import pandas as pd
import numpy as np

df=pd.read_csv("train.csv")

def ordinalencoder(df,column_name):
    distinct_values=set(df[column_name])
    c=0
    d={}

    for i in distinct_values:
        d[i]=c
        c+=1
    print(d)

    df[column_name]=df[column_name].map(d)

ordinalencoder(df,"SaleCondition")
print(df["SaleCondition"])
