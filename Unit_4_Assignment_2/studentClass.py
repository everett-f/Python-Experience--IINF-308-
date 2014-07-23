'''
Created on Apr 25, 2014

@author: Everett
'''
############Student Class##############################
class student(object):
    #static variables/class variables
    count = 0 
    ageSum = 0 
    
    def __init__(self,name,ID,age):
        self.name = name
        self.ID = ID
        self.age = age
        student.count += 1 #keeps track of how many instances are created
        student.ageSum += age #keeps total age 
    
#################END Student CLASS######################


#############Student School Class########################
class studentSchool(student):
    def __init__(self):#initialize instance variables
        self.sList = [] #keeping students in a list
        self.count = 0
        self.sumAge = 0
        
    def addStudent(self,student): #adds student instance to a list, changes count and sum of age
        self.sList.append(student)
        self.count += 1
        self.sumAge += student.age
        
        
    def printStats(self): #when called, prints stats of this instance
        print "Total Students:",self.count
        print "Average Age:",self.sumAge/float(self.count)
        
    
    def printAllSchoolStudentInfo(self): #When called, prints all students in this instance list
        print ("\n%6s%4s%4s")%("NAME","ID","AGE")
        for student in self.sList:
            print ("%6s%4d%4d")%(student.name,student.ID,student.age)
        self.printStats() #prints stats
##############END StudentSchool Class########################  
     
#making new schools  
toga = studentSchool()
shen = studentSchool()             

# Create student instance and adding students to saratoga(all male and young)
toga.addStudent((student("Bill",0,18)))
toga.addStudent((student("James",1,20)))
toga.addStudent((student("Eric",2,25)))
toga.addStudent((student("Pat",3,22)))

#Create student instances and adding students to Shen(All women and older)
shen.addStudent((student("Kat",38,44)))
shen.addStudent((student("Jane",99,32)))
shen.addStudent((student("Tessa",32,44)))
shen.addStudent((student("Genna",15,90)))

####Prints student count and average using static variables from class variables
print "-----Student instance------------"
print "Student Instances:",student.count
print "Student Average:",student.ageSum/float(student.count)

####Prints all students and stats using class functions
print "\n\n\n----Student School Instance------------"
toga.printAllSchoolStudentInfo()#print saratoga student info
shen.printAllSchoolStudentInfo()#print shen student info



