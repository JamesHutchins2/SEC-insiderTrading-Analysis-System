import pandas as pd 
import numpy as np
import os


#   In: A string 

#   Out: true, if 4 is the only char other than spaces, and false otherwise
length = 18879280
j = 0
for i in df.index:
    precent = i/length * 100
    j = j +1
    if j > 1000:
        print(precent)
        j = 0
    #get the current row
    row = df.loc[i]
    #get the form tyoe
    formType = row['Form Type']
    s = str(formType)
    s = s.strip()

    if len(s) != 1:
       
        #remove the row
        df.drop(i)
    if s == '4':
        continue
    else:
        
        #remove the row
        df.drop(i)