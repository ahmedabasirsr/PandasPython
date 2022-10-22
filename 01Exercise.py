import numpy as np
import pandas as pd


########################### Add new column in table#############################################################
stud = {"st_id":[100,101,103,104,105],
        "st_name":["Ahmed","Ali","Husian","Omar","Abas"],
        "st_marks":[480,570,470,510,490],
         "Average":[80,95,78.3,85,81.6]
        
    }
df = pd.DataFrame(stud) 
print("\t Add new column in table(Index[0,1..], st_id, st_name, Average)")
print("\n",df)
print("\n ",df["st_id"][0])
print("\n",df["st_name"][1])
print("\n",df["st_marks"][2])
print("\n",df["Average"][3])
df["st_id"][0]=500
df["st_name"][1]="Aliiiiiiii"
df["st_marks"][2]=600
df["Average"][3] =900
print("\n",df)



######################### 2 list convert to table(only 2 columns) with function Series#############################
######################### 1column=st_name 2column =st_marks #######################################################
st_name=["Ahmed","Ali","Husian","Omar","Abas"]
st_marks=[480,570,470,510,490]
######################### 1column=data 2column=index###############################################################
tabl = pd.Series(data=st_marks,index=st_name)
print("\n create table from 2 lists")
print("\n",tabl)
tabl["Ali"] =1000
tabl["Omar"]=2000
print("\n Access value with index=st_name","\n",tabl)
tabl[0] =100
tabl[1]=101
print("\n Access value with index=[0,1..]","\n",tabl)


