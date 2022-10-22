import numpy as np
import pandas as pd

stud = {"st_id":[100,101,103,104,105],
        "st_name":["Ahmed","Ali","Husian","Omar","Abas"],
        "st_marks":[480,570,470,510,490]
    }
x = pd.Series(stud)
print("convert dictionary to Series \n")
print(x,"\n")
print("\n view names: " ,x["st_id"])
print("\n view id: " ,x["st_name"])
print("\n view third id: " ,x["st_id"][2])
print("\n view four name: " ,x["st_name"][3])



