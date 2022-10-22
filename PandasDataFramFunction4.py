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

print(df_sheet1)

# unique is values they are not repeat
av=df_sheet1["average"].unique()
print("\n Print column average: ",av)

av1=df_sheet2["prosek"].unique()
print("\n Print column VI: ",av1)


#print(av + av1)
#newdata=pd.concat([av,av1]) is not clear how works
#s = newdata.unique()
#print("\n",s)


# join 2 frame in on(one after second
df_sheet3 = pd.concat([df_sheet1,df_sheet1],axis=1)
print(df_sheet3.head(30))
print(df_sheet3.columns)

    




#average Ученик Петар Шмигић VI prosek







    






















