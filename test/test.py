'''
Created on Feb 14, 2014

@author: Everett
'''


def oddOrEven():
    while True:
        try:
            num = int(raw_input("Please enter a number: "))
            break
        except:
            print "--------invalid input, Please try again--------"      
    if num % 2 == 0:
        print num,"is even"
    else:
        print num,"is odd"
    
# oddOrEven()

def unique():
    stack = []
    temp = []
    count = int(raw_input("how many numbers: "))
    for x in range(0, count):
        num = int(raw_input(str(x+1) + ") Please enter number: "))
        stack.append(num)
        if temp.count(num) > 0:
            stack.remove(num)
        elif stack.count(num) > 1:
            temp.append(stack.pop(stack.index(num)))
            stack.remove(num)          
    print stack
    print temp
    
# unique()


def numToRom():
    while True:
        num = int(raw_input("Please enter number between 1 and 10: ")) 
        try:
            print {
                    1:"I",
                    2:"II",
                    3:"III",
                    4:"IV",
                    5:"V",
                    6:"VI",
                    7:"VII",
                    8:"VIII",
                    9:"IX",
                    10:"X"
            }[num]
            break
        except:
            print "\n--------Number must be between and including 1 and 10--------"
                
# numToRom()

try:
    print 3/1
except:
    print "nope"
    
print "lame"
