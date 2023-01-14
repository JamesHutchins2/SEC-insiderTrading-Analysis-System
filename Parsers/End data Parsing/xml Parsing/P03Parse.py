import os 
import xml.etree.ElementTree as ET


def fileItter(path):
    #takes args: path to folder of files
    #returns: list of file names
    files = []
    for file in os.listdir(path):
        if file.endswith('.xml'):
            files.append(file)

    return files


def parseFile(file):
    file = formatFile(file)
    #takes args: file name
    #returns: dictionary of parsed data
    #import the xml file
    tree = ET.parse(file)
    root = tree.getroot()

    #create a dictionary to store the data
    data = {
        'issuerCik': None,
        'issuerName': None,
        'issuerTradingSymbol': None,
        'rptOwnerName': None,
        'rptOwnerCik': None,
        'rptOwnerStreet1': None,
        'rptOwnerStreet2': None,
        'rptOwnerCity': None,
        'rptOwnerState': None,
        'rptOwnerZipCode': None,
        'isTenPercentOwner': None,
        'isDirector': None,
        'isOfficer': None,
        'isOther': None,
        'officerTitle': None,
        
    }

    #parse the issuer table
    issuerData = getIssuer(root)
    print(issuerData)
    ReportingOwner = getReportingOwner(root)
    print(ReportingOwner)
    #not working only the first 3 values gotta fix it
    DerivTable = getDerivTable(root)
    print(DerivTable)

    #combine data into dict



    #parse the reporting owner table

    #parse the derivative Table (derivative transaction, -->(security title, transaction ammounts etc.) )

    #combine the data into a dictionary
def formatFile(file):
    content = ""
    with open(file, 'r') as f:
        content = f.read()
        start_index = content.index("<XML>")
        content = content[start_index:]
        end_index = content.index("</XML>")
        content = content[:end_index + len("</XML>")]
        #delete the second row
        content = content.splitlines()
        try:
            content.pop(1)
            content = "".join(content)
        except:
            print("file already formatted")
        #make content into a string 
        file = file.replace(".txt", "programReadable")
    try:
        with open(file, 'x') as f:
            f.writelines(content)
        with open(file, 'r') as f:
            content = f.readlines()
            content.insert(0, '<?xml version="1.0"?>')
        with open(file, 'w') as f:
            f.writelines(content)
    except:
        print("file already exists")
    
    
    
    return file

    #takes in a file and removes all outside of the XML tags
    #then moves the version tag to the top of the document 

def getIssuer(root):
    path = "d"
    data = [None] * 3
   
    for child in root.iter():

    #parse the issuer table
        if child.tag == 'issuer':
            for row in child.iter():
                if row.tag == 'issuerCik':
                    
                    issuerCik = row.text
                    data[0] = issuerCik
                if row.tag == 'issuerName':
                    issuerName = row.text
                    data[1] = issuerName
                if row.tag == 'issuerTradingSymbol':
                    issuerTradingSymbol = row.text
                    data[2] = issuerTradingSymbol
    
    return data




    #takes args: root of the xml tree
    #returns data from the issuer section

def getReportingOwner(root):
    #takes args: root of the xml tree
    #returns data from the reporting owner section

    data = [None] * 12
    for child in root.iter():
        if child.tag == 'reportingOwner':
            for row in child.iter():
                if row.tag == 'reportingOwnerId':
                    for each in row.iter():
                        if each.tag == 'rptOwnerName':
                            rptOwnerName = each.text
                            data[0] = rptOwnerName
                        if each.tag == 'rptOwnerCik':
                            rptOwnerCik = each.text
                            data[1] = rptOwnerCik
                if row.tag == 'reportingOwnerAddress':
                    for each in row.iter():
                        if each.tag == 'rptOwnerStreet1':
                            
                            rptOwnerStreet1 = each.text
                            data[2] = rptOwnerStreet1
                        if each.tag == 'rptOwnerStreet2':
                            
                            rptOwnerStreet2 = each.text
                            data[3] = rptOwnerStreet2

                        if each.tag == 'rptOwnerCity':
                            rptOwnerCity = each.text
                            data[4] = rptOwnerCity
                        if each.tag == 'rptOwnerState':
                            rptOwnerState = each.text
                            data[5] = rptOwnerState
                        if each.tag == 'rptOwnerZipCode':
                            rptOwnerZipCode = each.text
                            data[6] = rptOwnerZipCode
                if row.tag == 'reportingOwnerRelationship':
                    for each in row.iter():

                        if each.tag == 'isTenPercentOwner':
                            isTenPercentOwner = each.text
                            data[7] = isTenPercentOwner
                        if each.tag == 'isDirector':
                            isDirector = each.text
                            data[8] = isDirector
                        if each.tag == 'isOfficer': 
                            isOfficer = each.text
                            data[9] = isOfficer
                        if each.tag == 'isOther':
                            isOther = each.text
                            data[10] = isOther
                        if each.tag == 'officerTitle':
                            officerTitle = each.text
                            data[11] = officerTitle
    return data
    

def getDerivTable(root):
    data = [Node]*16
    #takes args: root of the xml tree
    for child in root.iter():
        if child.tag == 'derivativeTable':
            for row in child:
                if row.tag == 'derivativeTransaction':
                    for each in row:
                        if each.tag == 'securityTitle':
                            for val in each:
                                if val.tag == 'value':
                                    securityTitle = val.text
                                    data[0] = securityTitle
                                    
                        if each.tag == 'conversionOrExercisePrice':
                            for val in each:
                                if val.tag == 'value':
                                    conversionOrExercisePrice = val.text
                                    data[1] = conversionOrExercisePrice

                        if each.tag == 'transactionDate':
                            for val in each:
                                if val.tag == 'value':
                                    transactionDate = val.text
                                    data[2] = transactionDate
                        if each.tag == 'transactionCoding':
                            for val in each:
                                if val.tag == 'value':
                                    transactionCoding = val.text
                                    data[3] = transactionCoding
                        if each.tag == 'transactionAmounts':
                            for val in each:
                                if val.tag == 'value':
                                    transactionAmounts = val.text
                                    data[4] = transactionAmounts
                        if each.tag == 'transactionShares':
                            for val in each:
                                if val.tag == 'value':
                                    transactionShares = val.text
                                    data[5] =  transactionShares
                        if each.tag == 'equitySwapInvolved':
                            for val in each:
                                if val.tag == 'value':
                                    equitySwapInvolved = val.text
                                    data[6] = equitySwapInvolved
                        if each.tag == 'directOrIndirectOwnership':
                            for val in each:
                                if val.tag == 'value':
                                    directOrIndirectOwnership = val.text
                                    data[7] = directOrIndirectOwnership
        if child.tag == 'nonDerivativeTable':
                for row in child:
                    if row.tag == 'nonDerivativeTransaction':
                        for each in row:
                            if each.tag == 'securityTitle':
                                for val in each:
                                    if val.tag == 'value':
                                        securityTitle = val.text
                                        data[8] = securityTitle                            
                            if each.tag == 'transactionDate':
                                for val in each:
                                    if val.tag == 'value':
                                        transactionDate = val.text
                                        data.append(transactionDate)
                            if each.tag == 'transactionCoding':
                                for val in each:
                                    
                                    transactionCoding = val.text
                                    data.append(transactionCoding)

                            if each.tag == 'transactionAmounts':
                                
                                for val in each:
                                    if val.tag == 'transactionShares':
                                        
                                        for that in val:
                                            if that.tag == 'value':
                                                transactionShares = that.text
                                                
                                                data.append(transactionShares)
                                    if val.tag == 'transactionPricePerShare':
                                        for that in val:
                                            if that.tag == 'value':
                                                transactionPricePerShare = that.text
                                                data.append(transactionPricePerShare)
                                    if val.tag == 'transactionAcquiredDisposedCode':
                                        for that in val:
                                            if that.tag == 'value':
                                                transactionAcquiredDisposedCode = that.text
                                                data.append(transactionAcquiredDisposedCode)

                            
                            if each.tag == 'postTransactionAmounts':
                                for val in each:
                                    if val.tag == 'sharesOwnedFollowingTransaction':
                                        for that in val:
                                            if that.tag == 'value':
                                                sharesOwnedFollowingTransaction = that.text
                                                data.append(sharesOwnedFollowingTransaction)
                                        
                            if each.tag == 'directOrIndirectOwnership':
                                for val in each:
                                    if val.tag == 'value':
                                        directOrIndirectOwnership = val.text
                                        data.append(directOrIndirectOwnership)

    return data
                        
    #returns data from the derivative table






#xmlFiles/INAMED CORP0001244236-05-000017programReadable.xml