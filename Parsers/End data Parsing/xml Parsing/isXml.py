import os 
import re

def isXml(fileName):
    input_string = fileName
    start_index = input_string.index("-") + 1
    end_index = input_string.rindex("-")
    extracted_value = input_string[start_index:end_index]
    return(extracted_value) # "value"





