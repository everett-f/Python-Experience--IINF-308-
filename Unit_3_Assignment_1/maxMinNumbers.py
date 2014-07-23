'''
Created on Mar 3, 2014
Unit 3, Homework 2, Program 2
Purpose:    The purpose of this program is for the user to keep entering interger 
            numbers until user ends input by entering -99. The program
            will print the largest and smallest integer entered.
@author: Everett Franco
'''

large = None
small = None
errorMsg = "\n--------Error, Please try again--------"

while True: #loops until user enters acceptable inputs
    try:        
        num = input("Please enter a number(Enter -99 to exit): ")
        if num%2 != 0 and num%2 != 1: #checks to see if user input is a whole number
            raise # if  not a whole number, forces exception, restarts loop
        if num != -99:
            large = num #initializes large with first user input 
            small = num #initializes small with first user input 
        break
    except:
        print errorMsg
        
while num != -99: # ends loop when user enters -99
    try:        
        if num%2 == 0 or num%2 == 1: #checks to see if user input is a whole number
            if large < num: #checks for larger number, if so, replaces large
                large = num
            if small > num: #checks for smaller number, if so, replaces small
                small = num
        else: #if user enters decimal number, prints error
            print errorMsg
        num = input("Enter Number: ")   
    except:
        print errorMsg
        
#print results    
print "\n\nMaximum is:", large
print "Minimum is:", small    
