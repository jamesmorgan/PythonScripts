#!/usr/bin/python


##########################################################################
## Used to extract csv files and create a SQl files ready for inserting ##
##########################################################################

import csv
import array
import os

def createSqlFile( insertStatement ):
    file = open("never_dial_list.sql", 'w')
    file.write(insertStatement)
    file.close()

def readCsv( fileName ):
    file = open(fileName+'.csv', 'rb')
    file.next()
    return csv.reader(file, delimiter=',', quotechar='|')
    
insertStatement = "INSERT INTO `never_dial` (`TelephoneNumber`, `NeverDialContact`, `AddedDateTime`, `FK_UserID_AddedBy`, `Reason`) VALUES\n"

numbers = []

for row in readCsv('LeadX _Never_Dial_List'):
    numbers.append('0'+row[1])

for idx, number in enumerate(numbers):
    insertStatement += "('%s', 1, NOW(), '3338', 'Bad Number')" % (number,)
    eol = ',\n' if (idx + 1) != numbers.__len__() else ';'
    insertStatement += eol     

print insertStatement
createSqlFile(insertStatement)


