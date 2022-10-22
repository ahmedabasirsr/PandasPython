import numpy as np
import pandas as pd
import seaborn as snb
import matplotlib.pyplot as plt

# read file Excel sheet from path loction in variable 
# for that task you want to install seaborn and matplotlib
###########################################################
df_sheet = pd.read_excel("C:/Users/Nastavnik/Desktop/Projects/Pandas/VII Ocene.xlsx",
                   sheet_name="oc")
print(" convert file xlsx-sheet in DataFrame ")
#print(df_sheet)
#print(df_sheet.head(5))

df_sheet1 = pd.read_excel("C:/Users/Nastavnik/Desktop/Projects/Pandas/VII Ocene.xlsx",
                   sheet_name="za")
#print("\n",df_sheet.head(4))
#print(df_sheet.info)
#print (df_sheet.describe(include='all'))
print("DataFrame displays some statisc methodes ")
print (df_sheet.describe())

