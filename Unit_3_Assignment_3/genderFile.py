'''
Created on Mar 26, 2014

@author: Everett
'''
import re

def fileCheck():
    while True:
        try:
            fileName = raw_input("Please enter file name WITHOUT extension: ")#user input 
            with open(fileName+".txt","r") as fileObj: #open file
                strFile = fileObj.read()  #convert file to string
                strFileTest = strFile.strip("\n") #Remove newline characters from string
            
            if re.sub("[FM]","",strFileTest) != "": # If file isn't empty, creates new file or uses existing and writes correct version of old file to it
                goodFile = raw_input("File is not in correct format..\n"
                                     "Please enter new or existing file name WITHOUT extension: ")
                with open(goodFile+".txt","w") as goodFileObj: #open new or existing file for writing
                    strFile = re.sub("[^MF \n]","",strFile.upper()) #Removes everything but M's,F's and newline character
                    goodFileObj.write(strFile) #Writes correct version to new File
            return strFile #return corrected format string
        except Exception, e:
            print e       


def genderCount(strFile):
    fCount = float(strFile.count("F")) #counts F's
    mCount = float(strFile.count("M")) #counts M's
    total  = fCount + mCount #combined amount
    
    fRatio = fCount/total #Female ratio
    mRatio = mCount/total #Male ratio
    
    #Print results
    print ("Male ratio is: %.2f\n"
           "Female ratio is: %.2f")%(mRatio,fRatio)
###########CONTROL###########################
while True:
    strFile = fileCheck()
    genderCount(strFile)
    
    again = raw_input("\nAgain?(y/n): ").upper()
    if again == "N" or again == "NO":
        print "--Ending Program--"
        break
    elif again != "Y" and again != "YES":
        print"--Unrecognized input, Ending Program..--"
        break
################END CONTROl####################
