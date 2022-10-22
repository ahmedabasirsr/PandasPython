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

####view only average 5 in dataframe df_sheet1####
print("\n",df_sheet1[(df_sheet1["average"]==5)])


#### view student whose name is a Петар Шмигић
print("\n",df_sheet1[(df_sheet1["Ученик"]=="Петар Шмигић")])

#### add 5 in columm average
def average_5(marks):
    return (marks+5)


#print("\n",df_sheet1["average"].apply(average_5))
print("\n",df_sheet1.sort_values(by="average"))

    




#average Ученик Петар Шмигић







    






















