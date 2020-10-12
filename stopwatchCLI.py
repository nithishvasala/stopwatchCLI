
import os
import time

seconds = 0
minutes = 0
hours = 0

while(True):
    print("\t\t\t\t stop watch in python 3 by Nithish vasala")
    print("\n\n")
    print("\t\t\t-----------------------------------")
    print("\t\t\t %d : %d : %d " %(hours, minutes,seconds))
    print("\t\t\t-----------------------------------")
    time.sleep(1)
    seconds = seconds + 1

    if(seconds == 60):
        seconds = 0
        minutes = minutes + 1 

    if(minutes == 60):
        minutes = 0
        hours = hours + 1

    os.system('clear')
