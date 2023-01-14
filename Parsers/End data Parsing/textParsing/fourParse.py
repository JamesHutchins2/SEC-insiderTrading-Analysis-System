import os
import re
import pandas as pd
import numpy as np
import requests

#####################################
#This is the driver class for parsing files from before 2001, they are text format files 
# This class is used in the run.py file 
###########################################

#create a class
class Form4:
    #contructor
    def __init__(self, lines, name, dateFiled, relation, ticker, stateCompany, sNum, price, endoMowned, isDirect, tableOne, tableTwo, path):
        #got these 
        self.lines = lines
        self.name = name

        #parse from data 
        self.dateFiled = dateFiled

        
        #got this 
        self.relation = relation
        #got this 
        self.ticker = ticker
        #needed still
        self.stateCompany = stateCompany
        #needed still
        self.sNum = sNum
        #needed still
        self.price = price
        #needed still
        self.endoMowned = endoMowned
        #needed still
        self.isDirect = isDirect

        #gives path that the file is saved in 
        self.path = path
    

    def getLines(path):
        #IN: path to a file
        #OUT: a list of lines in the file
        file = open(path, 'r')
        lines = file.readlines()
        return lines
    
    
    def getName(lines):
        i = 0
        #IN: a list of lines in a file
        #OUT: the name of the Filing person
        for i in range(len(lines)):
            line = lines[i]
            if line.startswith('1.'):
                name = lines[i+1]
                return name
        

    #working
    def getCompanyName(lines):
        i = 0
        cName = ""
        for i in range(len(lines)):
            line = lines[i]
            if line.startswith('2.'):
                cName = lines[i+1]
                return cName
        
    
    def getCompanyTicker(lines):
        #IN: a list of lines in a file
        #OUT: the name of the company
        i = 0
        ticker = ""
        for i in range(len(lines)):
            line = lines[i]
            if line.startswith('2.'):
                company = lines[i+1]
                #print(company)
                #get the ticker from inside () in the company name
                try:
                    ticker = re.search(r'\((.*?)\)', company).group(1)

                except:
                    try:
                        company = lines[i +2]
                        ticker = company.strip()
                        if len(ticker) > 4:
                            ticker = "Not found"
                    except:
                        ticker = "Not found"
        #print(ticker)
        return ticker
       

    def getRelation(lines):
        #IN: a list of lines in a file
        #OUT: the relation of the Filing person
        i = 0
        for i in range(len(lines)):
            relation = ""
            line = lines[i]
            

            if line.startswith('6.'):
                
                relation = lines[i+1] + lines[i+2]
                
                relation = relation.split("(")
                if len(relation) <= 3:
                    relation = relation[0]
                    relation = relation.split("[")

                

                #print(relation)
                #remove all the white space
                for r in relation:
                    if r.startswith('X'):
                        relation = r
                        relation = relation.split()
                        
                    #split relation by the white space
                

                #take the second item
                try:
                    relation = relation[1]
                except:
                    relation = "Not found"
               
                
                break
        

        return relation
    
    def getTableOne(lines):
        data = []
        for i in range(len(lines)):
            line = lines[i]
            #go down 12
            if line.startswith('<S>'):
                
                j = i + 1
                stillData = True
                while stillData:
                    if lines[j].startswith('</TABLE>') or lines[j].startswith('     ') or lines[j].startswith('<CAPTION>'):
                        stillData = False
                        break
                    else:
                        data.append(lines[j])
                        j+=1
                    
                
                
                break

        return data
    def parseTable(data):
        for i in range(len(data)):
            #remove all spaces
            data[i] = data[i].replace(" ", "")
            #remove all "\n"
            data[i] = data[i].replace("\n", "")
        return data

    def getTableTwo(lines):
        data = [] 
        d = 1

        for i in range(len(lines)):
            line = lines[i]
            #go down 12
            if line.startswith('<S>'):
                if d == 0:
                    j = i +1
                    stillData = True
                    while stillData:
                        if lines[j].startswith('</TABLE>') or lines[j].startswith('     ') or lines[j].startswith('<CAPTION>'):
                            stillData = False
                            break
                        else:
                            data.append(lines[j])
                            j+=1
                    #get the data
                else:
                    d = 0
                
        return data


    def TableDecoder(table):
        #IN: a table of data
        #OUT: an array of scurity type, date filed, number of shares, price, value

        tableData = table.split(" ")
        #print(tableData)
        
    #method for getting the name





