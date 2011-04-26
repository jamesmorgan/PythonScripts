#!/usr/bin/python

###################################################################################### ##
## Used to fix / convert  all none case sensitive queries so can be ran on a linux box ##
#########################################################################################

import array
import os
import sys
import re

correctCaseWords = ['OfflineData',
                        'Title', 'Forename', 'Surname', 
                        'HomeTelephoneNumber', 'WorkTelephoneNumber', 'MobileTelephoneNumber', 
                        'DOB', 'EmailAddress', 
                        'Suppressed', 'SuppressedDateTime', 'SuppressedBy',
                        'Address1', 'Address2', 'Town', 'City', 'County', 'Postcode', 'HouseNumber', 'HouseName'
                        'SuspectText', 'SuspectName', 'Postcode', 'MobilePrefix', 'AreaCode', 'SuspectExemption'
                        'SuspectNameID', 'RequiredAction', 'InsertDate', 'ClosedDate', 'Checked',
                        'SuspectExemptionID', 'ExemptionName', 'ExemptionType', 'InsertDate',
                        'SuspectTextID', 'SuspectText', 'FK_DataAuditEntityID',
                        'DO_BuildWorkingLead', 'DobInvalid', 'NameInvalid', 'HomeTelephoneInvalid', 
                        'WorkTelephoneInvalid', 'MobileTelephoneInvalid', 'EmailInvalid', 'PostcodeInvalid']

#cffl = []
#for word in correctCaseWords:
#    regex = re.compile(word)
#    cffl.append(regex)

for path, subdirs, files in os.walk("..\."):
#for path, subdirs, files in os.walk("."):
    for name in files:
        if name.endswith(".sql"):
	        fhandle = open(os.path.join(path, name), 'r')
	        text = fhandle.read()
	        fhandle.close()
	        
	        for word in correctCaseWords:
	            text, count = re.subn(r'(?i)\b' + word + r'\b', word, text)
	            print word, count
	            
	        fhandle = open(os.path.join(path, name), 'w')
	        fhandle.write(text)
	        fhandle.close()
	        
            #print os.path.join(path, name)