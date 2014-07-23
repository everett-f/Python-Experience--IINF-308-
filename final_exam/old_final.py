'''
Created on May 9, 2014

@author: Everett
'''
import sqlite3 

conn = sqlite3.connect("phoneNumbers.db") #establish connection with database
curr = conn.cursor() #creates pointer to established database
curr.execute('DROP TABLE IF EXISTS People ') #drops table in database if the table 'People' already exist
curr.execute('CREATE TABLE People (firstName TEXT, lastName TEXT, phoneNumber TEXT)') # Creates table 'People'

likeQuery = "SELECT * FROM People WHERE lastName LIKE ? "
insertQuery = "INSERT INTO People (firstName, lastName, phoneNumber) VALUES (?, ?, ?)"

def query():# searches for name
    valid = {"YES","Y","YE"}
    again = "Y"
    while again in valid:
        lastName = raw_input("\nEnter last name to search for, or one or more characters of last name: ").strip()  
 
        queryResult ="" 
        for info in curr.execute(likeQuery,(lastName+"%",)): #for every row   
            queryResult += info[1]+", "+info[0]+": "+info[2]+"\n"#save row data to variable
    
        if queryResult: #if variable is not empty
            print queryResult #print results
        else: #otherwise
            print "No records were found matching your criteria '"+lastName+"'"
        
        
        again = raw_input("Search Again?(y/n)").upper()


try:
    phoneNumbersObj = open("phoneNumbers.txt","r") #Opens file for reading
except: #If file doesn't exist, prints error
    print "---Error, Cannot find file---\n" 
else:     
    skipLines = [] #holds skipped lines
    lineNum = 1 #keeps track of current line in txt file
    errorCount = 0 #counts errors
    
    for line in phoneNumbersObj: # for every line in txt file
        info = line.split() #puts each word in an list element
       
        if len(info) != 3: #if line is empty or line does not contain 3 words
            errorCount += 1 #increment error count by 1
            skipLines.append(lineNum) #add faulty line number to list
        else: #otherwise, insert data into table
            curr.execute(insertQuery, (info)) 
                 
        lineNum += 1 # increment line number
   
    phoneNumbersObj.close() #close file 
    conn.commit() #commit changes to database
    
    print errorCount,"error lines were detected and not processed:",skipLines #print results
    
    query() #calls query()
    
    conn.close() #disconnect from database


    

