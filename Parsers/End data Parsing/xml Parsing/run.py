from fourParse import Form4
import os

#this function creates a form4 object



#for each file in the directory
for file in os.listdir():
    if file.endswith(".txt"):
        #create a form4 object
        Lines = Form4.getLines(file)
        n = Form4.getName(Lines)
        #dateFiled = Form4.getDateFiled(Lines)
        relation = Form4.getRelation(Lines)
        ticker = Form4.getCompanyTicker(Lines)

        data = [ n, relation, ticker]
        print(data)
        #print the name of the person
        #print(data)
#parse the file








