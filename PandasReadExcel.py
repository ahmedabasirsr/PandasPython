import numpy as np
import pandas as pd
# read file Excel from path loction in variable "dfopenpyxl"
# for that task you want to install 
df = pd.read_excel("C:/Users/Nastavnik/Desktop/Projects/Pandas/Normal.xlsx")
print(" convert file xlsx in DataFrame ")
print(df)

print(" view frist 5 rows ")
print(df.head(5))

print("\n view last 6 rows ")
print(df.tail(5))
