import pandas as pd
import numpy as np
import os
import sys
import time
import datetime



path = "idxFiles"
files = os.listdir(path)
df = pd.DataFrame(columns=['Company Name', 'Form Type', 'CIK', 'Date Filed', 'File Name'])
i = 0
j = 0
masterArray = []


#counting precent complete
precent = 0
b = 0


for file in files:
    b = b+1
    if b > 500:
        print(f'precent complete: {precent/ 6200 * 100}%')
        b = 0
    precent = precent + 1
   
    if file.endswith(".idx"):
        with open(os.path.join(path, file), 'r') as f:
            link = ""
            CompanyName = []
            lines = f.readlines()
            for line in lines:
                #create an array of all values
                values = line.split(2*' ')
                

                name = ""
                formType = ""
                CIK = ""
                date = ""
                link = ""

                #name is alwasy the first value
                

                #remove empty values
                #print(len(values))
                #print(values)
                for value in values:
                    
                    if value == '':
                        values.remove(value)
                    if value == ' ':
                        values.remove(value)
                    if value == '  ':
                        values.remove(value)
                    
                #print(len(values))
                #print(values)


                #name
                name = values[0]

                #form typewillbe thenextindex that is not ""
                i = 2
                for i in range(len(values)):
                    if i == 0:
                        continue
                    if values[i] == '':
                        continue
                    else:
                        formType = values[i]
                        i = i+1
                        break
                
                #cik
                j = i
                for j in range(i,len(values)):
                    if values[j] == '':
                        continue
                    else:
                        CIK = values[j]
                        j = j+1
                        break
                
                #date
                k = j
                
                for k in range(j,len(values)):
                    if values[k] == '':
                        continue
                    else:
                        date = values[k]
                        k = k+1
                        break
                
                #link
                for l in range(k,len(values)):
                    if values[l] == '':
                        continue
                    else:
                        link = values[l]
                        l = l+1
                        break


                            


                



                items = [name, formType, CIK, date, link]
                #print(items)
                formType = formType.replace(' ', '')
                if formType == '4':
                    masterArray.append(items)

df = df.append(pd.DataFrame(masterArray, columns=['Company Name', 'Form Type', 'CIK', 'Date Filed', 'File Name']))
df.to_csv('masterForm4.csv', index=False)

