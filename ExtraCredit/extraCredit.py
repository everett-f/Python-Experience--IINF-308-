'''


@author: Everett
'''


def fileHandle(fileName):
    while True:
        try:
            if fileName == None:
                fileName = raw_input("\nPlease enter file name with extension: ")
            with open(fileName,"r") as fileObj:
                Sum = 0
                count = 0
                for line in fileObj:
                    if line.startswith("X-DSPAM-Confidence:"):
                        num = float(line.split()[1])
                        Sum += num
                        count += 1
                        print num
        except Exception, e:
            print e
            fileName = None
        else:
            average = Sum/count
            print("\nSum: %f\nAverage: %f")%(Sum,average)                   
            break               
            
            
while True:
    try:
        select = input("\nPlease select files:\n"
                        "Press 1 for: mbox.txt\n"
                        "Press 2 for: mbox-short.txt\n"
                        "Press 3 for: Other\n")
        if select < 1 or select > 3:
            raise    
    except:
        print "\n---Invalid Choice..Try again---"
    else:   
        if select == 1:
            fileName = "mbox.txt"
        elif select == 2:
            fileName = "mbox-short.txt"
        elif select == 3:
            fileName = None
                  
        fileHandle(fileName)
    
        again = raw_input("\nAgain?(y/n): ").upper()
        if again == "N" or again == "NO":
            print "--Ending Program--"
            break
        elif again != "Y" and again != "YES":
            print"--Unrecognized input, Ending Program..--"
            break
    
        
    
