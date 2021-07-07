import time

#Function will return the current time in the format:
#Hour : Minute : Second
def currentTime():
    return time.strftime("%H:%M:%S")
    
currentTime()

# Function will return the current date information in the format:
# Week Day, Day Month Year
def currentDate():
    return time.strftime("%a, %d %b %Y")
    
currentDate()