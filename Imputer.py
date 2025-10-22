import pandas as pd
import numpy as np



def imputer(df):
    #Finding columns with missing values 
    columns_with_missing=[]
    for col in df.columns:
        if df[col].isnull().any():
            columns_with_missing.append(col)
    
    #Finding mean values for those columns
    df1=df[columns_with_missing]
    mean_values=df1.mean(axis=0,numeric_only='True')

    mean_values_dict=mean_values.to_dict()
    
    
    #Imputing values
    new_df=df.fillna(mean_values_dict)
    return new_df

df=pd.read_csv("train.csv")
a=imputer(df)


 
