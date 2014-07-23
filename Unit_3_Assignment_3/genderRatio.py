'''
Created on Mar 26, 2014
Unit 3, Assignment 3
Purpose:  This program will prompt the user to enter in a text file name, where it will count the amount
          of capital M's and F's in that file, then print the ratio of them. If the File has extra characters
          other than M or F or newline. It will prompt the user to enter in a new or an existing file name
          to save the corrected changes.

@author: Everett
'''
import re #regex module

def fileCheck(): #checks file for format errors, if so, corrects them and prompts user for filename to save changes
    while True:
        try:
            fileName = raw_input("Please enter file name WITHOUT extension: ")#user input 
            with open(fileName+".txt","r") as fileObj: #open file
                strFile = fileObj.read().replace("\n","")  #convert file to string
            
            if re.sub("[FM]","",strFile) != "": # If file isn't empty, creates new file or uses existing and writes correct version of old file to it
                goodFile = raw_input("File is not in correct format..\n"
                                     "Please enter new or existing file name WITHOUT extension to save corrected format changes: ")
                with open(goodFile+".txt","w") as goodFileObj: #open new or existing file for writing
                    strFile = re.sub("[^MF]","",strFile.upper()) #Removes everything but M's,F's and newline character
                    goodFileObj.write(strFile) #Writes correct version to new File
            return strFile
        except Exception, e:
            print "-----------error----------\n",e       


def genderCount(strFile): # calculates male and female ratios
    
    total  = len(strFile) #combined amount
    fCount = strFile.count("F") #counts F's
    mCount = strFile.count("M") #counts M's


    if fCount != 0: #female ratio(checks to see if it divides by 0)
        print "Female ratio is:",float(fCount)/total
    else:
        print "No females"

    if mCount != 0: #Male ratio(checks to see if it divides by 0)
        print "Male Ratio is:",float(mCount)/total
    else:
        print "No Males"
    

###########CONTROL###########################
while True:
    genderCount(fileCheck()) #calls filecheck() then genderCount
    
    again = raw_input("\nAgain?(y/n): ").upper() #askes user to go again
    if again == "N" or again == "NO": #ends program if user enters N or NO
        print "--Ending Program--"
        break
    elif again != "Y" and again != "YES": #Ends program if user enters anything but Y or Yes
        print"--Unrecognized input, Ending Program..--"
        break
################END CONTROl####################
