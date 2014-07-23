'''
Created on Apr 26, 2014
Unit 4, Assignment 3
Purpose: The purpose of this program is to count how many different occurrences 
         of different words there are in an online book in txt format. The program
         will push the results into results.txt. Which is located in the same
         file directory as this program.

@author: Everett Franco
'''
import urllib #used for retrieving online content


wordDict = {} # initialize dictionary {word(key):occurrence(value)}
url = "http://www.gutenberg.org/files/27827/27827-8.txt" # url location for the book 'The Kama Sutra of Vatsyayana'

try:
    textObj = urllib.urlopen(url) #Opens connection and saves it to object
    for line in textObj: #for each line in website
        line = line.strip()#Removes \n
        if line == "": continue #skips empty lines
            
        words = line.split() # put each word in an list
        for word in words: #for each word in words
            letterList = list(word.upper()) # puts each capitalized  letter in an list
            
            for index, letter in enumerate(letterList): # for each letter in letterList 
                if not letter.isalpha(): #if letter is not alpha, it removes that character
                    letterList[index] = ""
                                                   
            word = "".join(letterList) #joins letterList back into a string        
            if word: #if word is not empty        
                if word in wordDict:#if word is in wordDict,increments value by 1
                    wordDict[word] += 1
                else: #word not in wordDict, adds word to wordDict and sets value to 1
                    wordDict[word] = 1 
                                   
    textObj.close() #closed connection

    with open("results.txt","w") as fileObj: #creates or overwrites filename result, and saves as an object      
        for key in sorted(wordDict): #sorts keys in wordDict alphabetically. for each key..
            fileObj.write("%30s%8s\n" % (key,wordDict[key])) #write to file, the key, then find the value of that key and write that next to key
            
    print "---results.txt Complete---" # prints once complete
    
except Exception,e:
    print "----------Error-----------\n",e