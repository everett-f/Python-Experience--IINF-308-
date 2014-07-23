'''
Created on Feb 25, 2014
Unit 2:  Assignment 3
Purpose: The purpose of this program is to find the speed that sound travels
         through in three different mediums(air, water or steel). 
@author: Everett Franco
'''
import sys
#############Error Formats############################
errorTemp = lambda e: ((19 * "-") + "ERROR" + (20 * "-") + "\n"  # Quick error format function
                       + str(e) + "\n" + (44 * "-") + "\n")
errorInput = lambda e: ((19 * "-") + "ERROR" + (20 * "-") + "\n"
                        "Invalid Input.. Please try again.\n"  # Quick error format function
                        "(" + str(e) + ")\n" + (45 * "-") + "\n")
#############END Error Formats########################

########Medium Speed Functions: PARAM(distance) returns list(FLOAT time, STRING medium name)########
def getSpeedAir(distance):  # Returns a list: Contains speed of sound traveling through Air given distance, and medium
    try:
        return (distance / 1100.0, "Air")
    except Exception, error:
        print errorTemp(error)
        sys.exit(1)

def getSpeedWater(distance):  # Returns a list: Contains speed of sound traveling through Water given distance, and medium
    try:
        return (distance / 4900.0, "Water")
    except Exception, error:
        print errorTemp(error)
        sys.exit(1)
        
def getSpeedSteel(distance):  # Returns a list: Contains speed of sound traveling through Steel given distance, and medium
    try:
        return (distance / 16400.0, "Steel")
    except Exception, error:
        print errorTemp(error)
        sys.exit(1)        
##########################################END Medium Speed Functions####################################   

########User Input######## 
while True:  # loops user input until correct or valid input is given
    try:
        medium = input("Please Choose the medium the sound wave will be traveling through.\n"  # user enters medium(1 for air, 2 for water or 3 for steel)
                               " -Enter 1 for air\n -Enter 2 for water\n -Enter 3 for steel\n")
        if(medium > 0 and medium < 4):  # if 1,2 or 3, continue onto next block. If not, loops back for retry
            break
        else:
            print "\n--------Incorrect Choice.. Please try again--------"
    except Exception, error:
        print errorInput(error)
                
while True:  # loops user input until correct or valid input is given
    try:
        distance = input("Please Enter the distance in feet traveled by a sound wave."  # user enters an integer value for distance
                                 "(Greater than 20,000 feet)\n")
        if(distance > 20000):  # if distance is greater than 20,000,  breaks out of loop and continues onto next block
            break
        else:
            print "\n--------Distance is not greater than 20,000 feet.. Please try again--------"
    except Exception, error:
        print errorInput(error)       
########End User Input########

#################Control and Results##########################
########Dictionary########
medTime = {  # saves returned list results(FLOAT time, STRING medium name) according to medium 
 1:getSpeedAir(distance),
 2:getSpeedWater(distance),
 3:getSpeedSteel(distance)
}[medium]
########End Dictionary########

print ("\n-------------------------Results-------------------------\n"
       "It will take %.10f seconds for the sound wave\nto travel in %s "  # Prints result
       "for a distance of %d feet.\n") % (medTime[0], medTime[1], distance)
#################END Control and Results#######################