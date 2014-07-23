'''
Created on Apr 5, 2014
Unit 3, Assignment 4
Purpose: This program will take in user input, and compare the given input to 
         the correct answers that have been hardcoded. It will then print the 
         results 
@author: Everett Franco
'''

examAnswers = ["B","D","A","A","C","A","B","A","C","D"] #Correct Answers
ansLen = len(examAnswers) #length of examAnswers(10)
validAns = ("A","B","C","D") #acceptable inputs

def gradeExam(): 
    wrongAns = [] #Initialize students wrong answers
    studentAnswers = [] #Initialize students answers
    index = 0 
    
    print "Please enter student answers(A, B, C, or D):"
    while index < ansLen: #While index is less than total answers
        try:
            sAns = raw_input(str(index+1)+". ").strip().upper() #User inputs answer
            if sAns in validAns: #if user input is in validAnswer list
                if examAnswers[index] != sAns: #if user answer does not match current exam answer
                    wrongAns.append(index + 1) #adds incorrect answer number to wrongAnswer list           
                studentAnswers.append(sAns) #adds answer to StudentAnswer list
                index += 1 
            else: #if user input is not a valid answer
                raise 
        except:
            print "\n---Invalid Input.. Please try again---"
    
    wrong = len(wrongAns) #counts amount of wrong answers 
    right = ansLen - wrong #gets amount of right answers
    status = "Passed" if wrong <= 4 else "Failed" # if more than 4 wrong, Failed, otherwise Passed
    questionsMissed = wrongAns if wrongAns else "None" #if wrongAns is not empty, saves list to questionsMissed, otherwise saves 'None' to question list
    
    print "\n\n"+status #Prints either 'Passed' or 'Failed'  
    print "Total Correct:",right #Prints amount of correct answers
    print "Total Incorrect:", wrong #Prints amount of wrong answers
    print "Questions Missed:",questionsMissed #Prints question numbers that were incorrect
    
    print ("\n%10s%8s%8s")%("Answers","Yours","Wrong") #Print Heading
    for i, x in enumerate(examAnswers): #prints numbered right and wrong answers
        ansNum = i+1
        flag = "X" if ansNum in wrongAns else ""
        print("%2d)%7s%8s%8s")%(ansNum,x,studentAnswers[i],flag)
        
        
###########CONTROL###########################
while True:
    gradeExam() #calls function
    
    again = raw_input("\nAgain?(y/n): ").upper() #askes user to go again
    if again == "N" or again == "NO": #ends program if user enters N or NO
        print "--Ending Program--"
        break
    elif again != "Y" and again != "YES": #Ends program if user enters anything but Y or Yes
        print"--Unrecognized input, Ending Program..--"
        break
    else:
        print"--Restarting Program--\n\n"
################END CONTROl####################

    

