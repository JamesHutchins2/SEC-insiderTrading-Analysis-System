import os 
from P03Parse import *
import xml.etree.ElementTree as ET
import pandas as pd

#import test 2
path = 'xmlFiles'

#call format file 
testPath = 'xmlFiles/INAMED CORP0001244236-05-000017.txt.xml'

data = parseFile(testPath)
print(data)




#for each file in xmlFiles
for file in os.listdir(path):
    print(file)
    if file.endswith('.xml'):
        #parse the file
        data = parseFile('xmlFiles/' + file)
        print (data)