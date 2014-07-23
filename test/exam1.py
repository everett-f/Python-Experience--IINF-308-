"""
Test 2
Description:   This file contains two programs. the first program genterates three random numbers between 1 and 100 and lists them. It also shows the smallest and largest number
                The second program calculates a balance according to the amount of checks and current balance entered in by the user. It runs a series of tests to see if it needs to duduct
                from the account balance
Author:        Everett Franco
"""

##################Program 1##############################
import random
import sys
#random number list
large = 0 #small variable
small = 100 #large variable

for x in xrange(0,3): #Loops 3 times
    num = random.randint(1,99)
    print num,
    if num > large:
        large = num
    if num < small:
        small = num
#     randNum.append(random.randint(1,99))#adds random number(1 - 99) to randNum
#     if randNum[x] >= large: #if randum number is bigger than large, it will replace large
#         large = randNum[x] #replaces large
#     if randNum[x] < small:#if randum number is smaller than small, it will replace small
#         small = randNum[x] #replaces small
#     print randNum[x],#prints random numbers
print("\nThe largest is: %d\nThe smallest is: %d\n\n")%(large,small)#prints largest and smallest random number
    

###################END PROGRAM 1####################################


######################PROGRAM 2######################################
def account(balance,checks): #calculates balance total
    if checks >= 1 and checks <= 100: #if checks are between 1 and 100
        if balance < 400: #deduct $15 if balance is smaller than $400
            balance -= 15.0            
        balance -= 10.0 #deduct $10 monthly charge
        if checks < 20: #if number of checks are less than 20 
            balance -= ((.10)*(checks)) #deduct checks*.10 to balance
        elif checks >= 20 and checks <= 39:#if number of checks are between 20 and 39 
            balance -= ((.08)*(checks)) #deduct checks*.08 to balance
        elif checks >= 40 and checks <= 59:#if number of checks are between 40 and 59 
            balance -= ((.06)*(checks)) #deduct checks*.06 to balance
        elif checks >= 60:#if number of checks are 60 or more 
            balance -= ((.14)*(checks)) #deduct checks*.14 to balance
        return balance 
    else: # if checks aren't between 1-100, print error and end program
        print "--------Error.. Check count isn't between 1-100--------\n"
#         exit(1)
        #quit()
        sys.exit(1)

try: #user input
    balance = float(raw_input("What is your balance?:\n"))
    checks = float(raw_input("How many checks have you written?:\n"))
except: # if user input are not floats
    print "--------Input error--------"
else: #Prints results
    print ("Your balance amount is: $%.2f")%(account(balance, checks))
######################END PROGRAM 2####################################


    
    
