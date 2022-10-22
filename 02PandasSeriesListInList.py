import numpy as np
import pandas as pd
###############################################################
# 2 list convert to table with function Series==> only 2 columns
# 1 Column index=set_name, 2Column list of marks
###############################################################

st_name=["Ahmed","Ali","Husian","Omar","Abas"]
st_marks=[[50,55,60,65],[70,75,80,90],[90,95,85,75],[60,55,90,80],[100,90,95,90]]
tab2 = pd.Series(data=st_marks,index=st_name)
print("\n create table2 from 2 lists")
print("\n",tab2)

print ("\n Serach from index => st_name: ",tab2["Omar"])
print ("\n Serach from index => st_name: ",tab2["Ali"])
print ("\n Serach from index => st_name: ",tab2["Ali"][1])
print ("\n Serach from index => st_name: ",tab2["Ali"][3])

print("\n print marks for every index- first column")
for i in tab2:
    print(i)

print("\n print marks for every index- first column")
for i in range(len(tab2)):
    print (tab2[i])
    
   

