'''
Created on Mar 22, 2014
Purpose: The purpose of this program allows for the user to pick between 6 different
         string functions that allow for manipulation or information regarding the 
         input string.
@author: Everett Franco
'''
import re  # regex module
#################################FORMAT FUNCTIONS#################################################
exceptError = lambda(e): 20 * "-" + "Error" + 20 * "-" + "\n" + str(e) + "\n\n"  # Prints exception error if exception occurs

def isEmpty(word): #Checks to see if user input is empty. If so, returns true with error messege, false, returns false
    if word == "" or word == None:
        return (True,"---Nothing entered.. Please try again---\n")
    else: 
        return (False,"")
#################################END FORMAT FUNCTIONS##############################################

#################################STRING FUNCTIONS#################################################
def phraseToAcronym(): # Converts user input into an acronym
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
            print exceptError(e)  # Prints exception error if exception occurs
           
    for x in cutUp:  # takes first letter of each list element, capitalizes them, then adds it to the variable Acronym
        acronym += x[0].upper()
    
    # prints results
    print "\nOriginal Phrase:", phrase
    print "Acronym:", acronym

def isPalidrome(): #Checks user input if it's a palidrome or not
    while True:
        try:
            word = raw_input("\nPlease enter a word to check if it's a Palindrome: \n").upper()
            emptyCheck = isEmpty(word) #check if input is empty
            if emptyCheck[0]:
                print emptyCheck[1]
                continue
            
            isPal = True
            test = re.sub('[^A-Za-z0-9]', '', word) #removes whitespace characters and special characters
            wordLen = len(test) #how many letters
            halfIndex = (wordLen/2) #half the letters
            
            for i, x in enumerate(test): #Loops through each letter in user input
                if i == halfIndex: #stops halfway to prevent redundancy
                    break
                if x != test[(wordLen-1)-i]: #checks each letter from corrasponding sides to see if they're the same
                    isPal = False
                    break
            if isPal: #print results
                print 'The word "'+word+'" IS a palindrome\n'
            else:
                print 'The word "'+word+'" is NOT a palindrome\n'
                
            break
        except Exception, e: 
            print exceptError(e)
            
def wordCount(): #Counts the amount of words given by user
    while True:
        try:
            para = raw_input("\nPlease enter a sentence or paragraph for word count:\n\n") 
            emptyCheck = isEmpty(para) #check if input is empty
            if emptyCheck[0]:
                print emptyCheck[1]
                continue       
            para = para.split() #splits each word into a list element
            count = len(para) #counts amount of list elements
            print "\nThere are",count,"word(s) in your sentence"
            break
        except Exception, e:
            print exceptError(e)
            
def reverseLetters():
    while True:
        try:
            letters = raw_input("\nPlease enter a sentence or paragraph for the letters to be reversed:\n\n")
            emptyCheck = isEmpty(letters) #check if input is empty
            if emptyCheck[0]:
                print emptyCheck[1]
                continue 
            print letters[::-1] #reverses letters in given word
            break
    
        except Exception, e:
            print exceptError(e)
            
def reverseWords():
    while True:
        try:
            words = raw_input("\nPlease enter a sentence or paragraph for the words to be reversed:\n\n")
            emptyCheck = isEmpty(words) #check if input is empty
            if emptyCheck[0]:
                print emptyCheck[1]
                continue 
            
            words = words.split() #converts each word into an element in a list
            sentLen = len(words)-1 #gets string length
            half = sentLen/2 #halves string length
            count = 0
                    
            while count <= half: #while count is less than or equal to half(prevents redundancy)
                temp = words[count] #Store current index value in temp
                words[count] = words[sentLen] #Replace current index value with corrosponding index value
                words[sentLen] = temp #replaces corrosponding index value with current index value
                count += 1 #increment current index
                sentLen -= 1 #decrement corrosponding index
                  
            print " ".join(words) #joins array elements into single string, print results
            break
        
        except Exception, e:
            print exceptError(e)
            
def unique():
    while True:
        try:
            unique = raw_input("\nPlease enter a word or sentence to count amount of unique letters and numbers:\n").upper()  
            emptyCheck = isEmpty(unique) #check if input is empty
            if emptyCheck[0]:
                print emptyCheck[1]
                continue 
            
            unique = re.sub("[^A-Za-z0-9]","",unique) #Removes all whitespace and special characters
            data = [] #initilize tuple list
            
            for x in unique: 
                count = unique.count(x)
                if (x,count) not in data: #if tuple does not exist in list, appends tuple to list
                    temp = (x,count)
                    data.append(temp)
            print("\n%s%10s")%("Letter","Count") #prints result
            for x in data:
                print("%s %10d")%(x[0],x[1])

            break
        except Exception, e:
            print exceptError(e)
##############################END STRING FUNCTIONS############################
                
                
############################CONTROL##########################################
while True:        
    try:
        choice = input("\n-Please enter appropriate number for the following-\n" #promps user to pick string routine 
                       "-Press 1 for Acronym:\n"
                       "-Press 2 for Palidrome:\n"
                       "-Press 3 for Word Count:\n"
                       "-Press 4 for Reverse Letters:\n"
                       "-Press 5 for Reverse Words:\n"
                       "-Press 6 for Unique Characters:\n")
        if choice == 1: #calls function according to user input
            phraseToAcronym()
        elif choice == 2:
            isPalidrome()
        elif choice == 3:
            wordCount()
        elif choice == 4:
            reverseLetters()
        elif choice == 5:
            reverseWords()
        elif choice == 6:
            unique()
        else:
            raise
    except:
        print"\n---Invalid choice, please try again---"
        continue
       
    try:
        again = raw_input("\n\nAgain?(y/n): ").upper() # Askes user if they wish to try again or end program
        if again == "N" or again == "NO":
            print "--End Program--"
            break
        elif again != "Y" and again != "YES":
            raise
    except:
        print"--Unrecognized input, Ending program..--"
        break
        
#########################END CONTROL##############################################