#   Assignment 1, Program 2
#   Program prints a pattern of forward and back slashes according to the amount of even lines given.
#   Name: Everett Franco

lines = int(raw_input("how many lines(must be even)?(Enter 6 for correct answer)\n"))#user input
half = lines/2      #half lines 
########Begin SpikeyLines Function##############
def spikeyLines(lines, slashCount = 1, space = lines/2):
    if (lines > 0):            #checks to see if the lines amount are not 0, if so, it continues onto the function, else, it jumps out of the function
        if lines > half:       #checks to see if halfway, if so, contiues to else statement
            print(" "*space)+(("\\"*slashCount)+("/"*slashCount))   #prints upper half slash pattern 
            return spikeyLines(lines-1, slashCount+1, space-1)
        else:
            print(" "*(space+1))+(("/"*(slashCount-1))+("\\"*(slashCount-1)))   #prints lower half slash Pattern
            return spikeyLines(lines-1, slashCount-1, space+1)    
########END SpikeyLines Function###############

spikeyLines(lines) #calls spikeyLines Function

