"""
Unit 2  Homework 2
Purpose:       The purpose of this program is to decide a internet and cable packaged
                 based on the user requirments
Description:   Picks best fit package for customer
Name:          Everett Franco
"""              


     
while True:
    try:     
        speed = int(raw_input("Enter the download internet speed that you require.\n"  # Mbps input
                              "Please enter a range from 3 to 20 Mbps: "))  
        if (speed >= 3) and (speed <= 20):  # Tests if input is between and including 3 and 20
            break  # Breaks out of loop if correct
        else:
            print "-------- Not between 3 and 20, try again--------"
    except:
        print "-------Invalid speed, try again--------"

while True:
    try:    
        channel = int(raw_input("Enter the number of TV channels you require.\n"  # Channel input
                                "Please enter a number in the range from 5 to 250: "))  
        if (channel >= 5) and (speed <= 250):  # Tests if input is between and including 5 and 250
            break
        else:
            print "--------Not between 5 and 250, try again--------"
    except:
        print "--------Invalid channel, please try again--------"  # Prints error
                
if (speed >= 3 and speed <= 13):  # Includes packages 1-5 with Mbps ranging between 3 and 13
    if (channel >= 5 and channel <= 70):  # 1st package criteria met
        print ("We recommend: TRIPLE STANDARD TV & BASIC INTERNET "
              "for $89.99 per Month")
    elif (channel >= 71 and channel <= 150):  # 2nd package criteria met
        print ("We recommend: DIRECTV, INTERNET & PHONE(CHOICE 150 CHANNELS) "
              "for $84.97 per Month")
    elif (channel >= 151 and channel <= 199):  # 3nd package criteria met
        print ("We recommend: DIRECTV, INTERNET & PHONE(XTRA 210 CHANNELS) "
              "for $89.97 per Month")
    elif (channel >= 200 and channel <= 210):  # 5nd package criteria met
        print ("We recommend: TRIPLE BASIC INTERNET "
              "for $99.99 per Month")
    else:  # 4th package criteria met
        print ("We recommend: DIRECTV, INTERNET & PHONE(ULTIMATE 225 CHANNELS) "
              "for $94.97 per Month")
else:  # if user wants more than 13Mbps, they'll have to choose #6, No matter how many channels they want
    print ("We recommend: TRIPLE WITH TURBO INTERNET "
           "for $129.99 per Month")   

