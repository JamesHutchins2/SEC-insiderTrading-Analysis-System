import os 
import re
import xml.etree.ElementTree as ET
import pandas as pd
#call supporting fucntion from main 

def parseTable(root):
    derivativeData  = parseDerive(root)
    nonDerivativeData = parseNonDerive(root)

#find derivative table and parse 
def parseDerive(root):
    #for parsing derivative security transactions

#find non derivative table and parse
def parseNonDerive(root):
    for child in root:
        if child.tag == 'derivativeTable':
            ndTransaction = []
            for each in child:
                if each.tag == 'nonDerivativeTransaction':
                    ParseNDTreansaction(each)
                    #we will now parse the non derivative transaction
    return(ndTransaction)


def ParseNDTreansaction(each):
    ndTransaction = [None]
    for child in each:
        if child.tag == 'securityTitle':
            for each in child:
                if each.tag == 'value':
                    ndTransaction[0] = each.text
            
        if child.tag == 'transactionAmounts':
            for each in child:
                if each.tag == 'transactionShares':
                    for that in each:
                        if that.tag == 'value':
                            ndTransaction[0] = that.text
                if each.tag == 'transactionPricePerShare':
                    for that in each:
                        if that.tag == 'value':
                            ndTransaction[0] = that.text
                if each.tag == 'transactionAcquiredDisposedCode':
                    for that in each:


     