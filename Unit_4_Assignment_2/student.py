'''
Created on Apr 24, 2014

@author: Everett
'''
from itertools import count

class student(object):
       
    def __init__(self,name,ID,age):
        self.name = name
        self.ID = ID
        self.age = age

    def studentInfo(self):
        print ("%6s%4d%4d")%(self.name,self.ID,self.age)
        
       
class school(student):
    _count = count(1)
    # _list = []
    
    def __init__(self,array):
        self.count = self._count.next()
        self._list = []
        self._list.append(student)

         
  
bill = student("Bill",0,18)
sally = student("Sally",1,20)
dan = student("Dan",2,22)

toga = school(bill)
toga = school(sally)
moh = school(dan)

print toga._list[0].name
print toga._list[0].name

print moh._list[0].name



#sList =[]
'''
student("Bill",0,18).addToList()
a = student("Sally",1,20)
a.addToList()
print a._list[0].name
'''
'''
sList.append(student("Bill",0,18))
sList.append(student("Sally",1,20))
sList.append(student("eric",2,17))
sList.append(student("joe",3,15))
sList.append(student("tim",4,19))
sList.append(student("james",5,18))
sList.append(student("gabe",6,22))
sList.append(student("jean",7,21))

print sList[len(sList) -1].count


print ("%6s%4s%4s\n")%("NAME","ID","AGE")
for student in sList:
    student.studentInfo()
  
#print sList.getAgeSum()
'''