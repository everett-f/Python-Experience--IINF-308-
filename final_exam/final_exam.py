'''
Created on May 9, 2014
Final Exam Part 2
Purpose: The purpose of this program is to read in a txt file containing information
         about people, including their first and last name and phone number. The
         program will check if there is missing data or an empty line from the
         txt file. For each line that is without error, it will insert the information
         into the database 'phoneNumbers.sqlite' into the table 'People'. The user will 
         then be asked to enter a persons last name to be searched for. The program will
         display all rows that contains that persons last name or like it. Otherwise it 
         will display that it has no person matching the criteria.
@author: Everett Franco
'''
import sqlite3 

class DBManager(object):#db manager class
    def __init__(self,DB): #default is phoneNumbers.db
        self.DB = DB
        
    def openDB(self):
        self.conn = sqlite3.connect(self.DB) #connects to database
        self.curr = self.conn.cursor() 

    def query(self,query,param = None): #Overloaded function used for execution
        if param:
            self.curr.execute(query,param) #if query has two parameters 
        else:
            self.curr.execute(query) #if query has 1 parameter
        return self.curr 
    
    def commitDB(self): #saves changes
        self.conn.commit()
        
        
    def closeDB(self): #close connection
        self.commitDB() #commits changes just in case programmer forgets to commit
        self.conn.close()


phone = DBManager("phoneNumbers.db") #create new instance of DBManager class

phone.openDB()
phone.query('DROP TABLE IF EXISTS People') #drops table 'People' if it exists
phone.query('CREATE TABLE People (firstName TEXT, lastName TEXT, phoneNumber TEXT)') # Creates table 'People'
phone.closeDB()

def query():# searches for name
    valid = {"YES","Y","YE"}
    again = "Y"
    while again in valid:
        lastName = raw_input("\nEnter last name to search for, or one or more characters of last name: ").strip()# Sanitizes before and after input of whitespace characters  
 
        queryResult ="" 
        phone.openDB()
        for info in phone.query("SELECT * FROM People WHERE lastName LIKE ? ",(lastName+"%",)): #for every row   
            queryResult += info[1]+", "+info[0]+": "+info[2]+"\n"#save row data to variable
    
        if queryResult: #if variable is not empty
            print queryResult #print results
        else: #otherwise
            print "No records were found matching your criteria '"+lastName+"'\n"
        phone.closeDB()      
        again = raw_input("Search Again?(y/n): ").upper()


try:
    phoneNumbersObj = open("phoneNumbers.txt","r") #Opens file for reading
except: #If file doesn't exist, prints error
    print "---Error, Cannot find file---\n" 
else:     
    skipLines = [] #holds skipped lines
    lineNum = 1 #keeps track of current line in txt file
    errorCount = 0 #counts errors
    
    phone.openDB()#open database
    for line in phoneNumbersObj: # for every line in txt file
        info = line.split() #puts each word in an list element
       
        if len(info) != 3: #if line is empty or line does not contain 3 words
            errorCount += 1 #increment error count by 1
            skipLines.append(lineNum) #add faulty line number to list
        else: #otherwise, insert data into table
            phone.query("INSERT INTO People (firstName, lastName, phoneNumber) VALUES (?, ?, ?)", (info)) 
                 
        lineNum += 1 # increment line number
   
    phoneNumbersObj.close() #close file 
    phone.closeDB() #commit changes to database
    
    print errorCount,"error lines were detected and not processed:",skipLines #print results
    
    query() #calls query()
    
    
    print "\n--End of Program--"
        





        
