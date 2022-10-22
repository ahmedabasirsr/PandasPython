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
#print(df_sheet1)

'''
# change values for column Average 
for x in df_sheet1.index:        # index to access the index data frame
    if df_sheet1.loc[x,"average"]<5: #to access the column
        df_sheet1.loc[x,"average"]=5
        #df_sheet1.loc[x,"average"]=y
        
print("\n",df_sheet1)
'''
print(df_sheet2)

for i in df_sheet2.index:
    if df_sheet2.loc[i,"prosek"]!=5:
       df_sheet2.loc[i,"prosek"] =5
       
print("\n",df_sheet2)
        
    



#Ученик Прво полугодиште Друго полугодиште 31. август average


















