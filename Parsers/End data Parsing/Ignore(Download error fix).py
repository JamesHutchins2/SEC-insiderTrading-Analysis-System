#this program determines weather a file is downloaded or not 
#if the file is remove this row of the df 

import pandas as pd
import os
import shutil
import time
import datetime
import sys

def name(row):
    link = row['File Name']
    name = row['Company Name']
    splitLink = link.split('/')
    #print(splitLink)
    number = splitLink[(len(splitLink)-1)]
    fileName = name + number + '.xml'
    return fileName

#import the data frame from the csv 
df = pd.read_csv('../cleaned4.csv')
#remove the first 32,000 rows
df = df[32000:]
#define path to folder with the files 
path = '../xmlFiles/'
#iterate through each row of the df
length = len(df)
i = 0
for index, row in df.iterrows():
    precent = i/length * 100
    print(f'precent complete: {precent}%')
    #determine file name from the row of the df 
    fileName = path + name(row)
    print(fileName)
    #if the file exists in the folder
    if(os.path.exists(fileName)):
        print("File already exists")
        #print("File already exists")
        #remove the row from the df 
        df.drop(index, inplace=True)


#save the df to a csv
df.to_csv('cleanedAndReduced.csv', index=False)
