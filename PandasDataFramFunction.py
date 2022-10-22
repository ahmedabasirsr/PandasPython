import numpy as np
import pandas as pd
import seaborn as snb
import matplotlib.pyplot as plt

# read file Excel sheet from path loction in variable 
# for that task you want to install seaborn and matplotlib
###########################################################
df_sheet1 = pd.read_excel("C:/Users/Nastavnik/Desktop/Projects/Pandas/VII Ocene.xlsx",
                   sheet_name="oc")

df_sheet2 = pd.read_excel("C:/Users/Nastavnik/Desktop/Projects/Pandas/VII Ocene.xlsx",
                   sheet_name="za")

####### view array columns of DataFrame df_sheet1
#print (df_sheet1.columns)

####### view table of DataFrame df_sheet1 => sum empty fields
#print(df_sheet1.isna().sum())

#######Fill fielde in average(mean)value
x = df_sheet1["IX"].mean()
#Fill fielde in value =0
df_sheet1["IX"].fillna(0,inplace=True)
#print(df_sheet1.isna().sum())

df_sheet1["X"].fillna(0,inplace=True)
print("\n",df_sheet1.isna().sum())


df_sheet1.dropna(subset=["III"],inplace=True)
print("\n",df_sheet1.isna().sum())


























