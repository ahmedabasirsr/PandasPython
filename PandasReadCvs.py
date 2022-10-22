import numpy as np
import pandas as pd
# read file csv from path loction in variable df
df = pd.read_csv("C:/Users/Nastavnik/Desktop/Projects/Pandas/grade.csv")
print(" convert file csv in DataFrame ")
#print(df)

print(" view frist 5 rows ")
print(df.head(5))

print("\n view last 5 rows ")
print(df.tail(5))
