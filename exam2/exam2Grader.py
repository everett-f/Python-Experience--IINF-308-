'''
Created on Apr 11, 2014
Exam 2 Grader
Purpose: This will take in two files and print the results of where the differences are
@author: Everett
'''

badPair = []
badLineList = []

try:
    
    print ("%4s%10s%10s")%("LINE","EXPECTED","FOUND")    
    with open("directions.txt","r") as originalObj, open("newDirections.txt","r") as resultDirObj:
        for lineNumber,(oLine,rLine) in enumerate(zip(originalObj,resultDirObj)):
            lineNumber += 1
            oList = oLine.split()
            rList = rLine.split()
            
            for i,(oWord,rWord) in enumerate(zip(oList,rList)):
                if oWord != rWord:
                    print ("%4d%10s%10s")%(lineNumber,oWord,rWord)
             
except Exception,e:
    print "---Error---\n",e    



    