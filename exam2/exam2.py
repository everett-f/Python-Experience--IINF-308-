"""
Exam 2
Auther: Everett Franco
Purpose: This program will read in a text file and encode it. It will print the
	 statistics and write the the revised text to the new file 'newDirections.txt'
Date:  4/10/14
"""
numReplaced = 0 #Counts lines that needed replacing
lineList = [] #keeps track of lines that needed replacing
wordDir = { #directory of key words to be replaced
        "left":"right",
        "South":"North",
        "third":"second"
        }

try:	
    with open("directions.txt","r") as dirObj, open("newDirections.txt","w") as newDirObj: #opens file for reading and newfile for writing
        for lineCount,line in enumerate(dirObj): #goes through each line in file and counts lines
            isPerfect = True #assumes line doesn't have any key characters
            space = "\t" if line.startswith("    ") or line.startswith("\t") else ""
            lineSplit = line.split() #splits lines to an list for each word

            for i,word in enumerate(lineSplit): #goes through each word in the split line
                if word in wordDir: #checks to see if word is in word directory
                    lineSplit[i] = wordDir[word] #replaces word with alternative word
                    numReplaced += 1 #increments numbers replaced
                    isPerfect = False
                     
            if isPerfect == False: #if line contains at least 1 fix, saves line number to lineList
                lineList.append(lineCount + 1) #adds numberline to list
                
            newDirObj.write(space+" ".join(lineSplit)+"\n") #joins list and adds it to the new File

except Exception,e:
    print "----------Error------------\n",e

else:
    #prints results
    print "---RESULTS---"
    print "Number of words replaced:",numReplaced
    print "Lines encoded:",lineList
