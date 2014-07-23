'''
Created on Mar 16, 2014
Unit 3, Assignment 2
Purpose: This program will take user input in the for of a sentence and convert
         it into an Acronym. It checks to to make sure user input contains more
         than one word and that the sentence does not contain digits.
@author: Everett Franco
'''
import re  # regex module
while True:
    acronym = "" 
    
    while True:  # Repeats until user enters valid input
        try:
            phrase = raw_input("\nPlease enter sentence to be converted into an Acronym:\n"
                           "(Must not contain digits and needs more than one word)\n\n")    
            cutUp = phrase.split()  # convert each word to a list element
            test = re.sub('[^0-9]', '', phrase)  # removes everything but numbers, so it can be tested with isdigit()
            if(not test.isdigit() and len(cutUp) > 1):  # if phrase contains no digits and phrase has more than one word, break loop and continue to next block
                break
            print "----Must Contain more than one word and Must contain no digits. Try again..\n"  # Prints error if phrase contains a digit or has one word
        except Exception, e:
            print 10 * "-" + "Error" + 10 * "-" + "\n" + str(e) + "\n\n"  # Prints exception error if exception occurs
           
    for x in cutUp:  # takes first letter of each list element, capitalizes them, then adds it to the variable Acronym
        acronym += x[0].upper()
    
    # prints results
    print "\nOriginal Phrase:", phrase
    print "Acronym:", acronym
    # Askes user if they wish to try again or end program
    again = raw_input("\n\nAgain?(y/n): ").upper()
    if again == "N" or again == "NO":
        break
    elif again != "Y" and again != "YES":
        print"--Unrecognized input, Ending program..--"
        break
