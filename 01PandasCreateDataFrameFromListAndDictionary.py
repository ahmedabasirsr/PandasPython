import numpy as np
import pandas as pd
'''
stud = {"st_id":[100,101,103,104,105],
        "st_name":["Ahmed","Ali","Husian","Omar","Abas"],
        "st_marks":[480,570,470,510,490]
    }

########################### This is Excel from python (create table from dictionary###############################
############################ 1column=index(0,1,..) 2column=st_id 3column=st_name 4column =st_marks 5column=Average  
df = pd.DataFrame(stud)
print("convert dictionary in table")
print("\n",df)

########################### Add new column in table#############################################################
stud = {"st_id":[100,101,103,104,105],
        "st_name":["Ahmed","Ali","Husian","Omar","Abas"],
        "st_marks":[480,570,470,510,490],
         "Average":[80,95,78.3,85,81.6]
        
    }
df = pd.DataFrame(stud) 
print("\n Add new column in table")
print("\n",df)

######################### 2 list convert to table with function Series#############################################'''
st_name=["Ahmed","Ali","Husian","Omar","Abas"]
st_marks=[480,570,470,510,490]
tabl = pd.Series(data=st_marks,index=st_name)
print("\n create table from 2 lists")
print(tabl)

