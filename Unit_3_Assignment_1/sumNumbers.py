'''
Created on Mar 3, 2014
Unit 3, Homework 1, Program 1
Purpose:    The purpose of this program is to sum all of the integers between 1 
            and the number given by the user.
@author: Everett Franco
'''
Sum = 0 
while True: #loops through until user enters acceptable input
    try:
        num = input("Please enter a non zero, non negative whole number:\n")
        if(num <= 0 or (num%2 != 0 and num%2 != 1)): #checks if number is an integer, an non zero and non negative number
            raise #if user input isn't acceptable, forces exception and restarts loop
        break
    except:
        print "\n\n--------Error, Please try again..--------"

for x in xrange(1, num+1): #starts at 1, increments by 1, ends at user input +1
    Sum += x # keeps adding the current number to the total amount

print "The sum is",Sum #print results
    
    
    

    
    