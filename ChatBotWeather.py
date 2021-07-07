'''ChatBot Weather feature'''

import requests #allows combiniation of code with web services - open weather map API                           

def WeatherConditions():
    choice = int(input("What you would like to see from the numbered options: "))  
    
############# Code Imported from: <https://www.youtube.com/watch?v=lcWfSn6-m_8> to use API services from weather map - modified code has comments at end of it 
  
    webadd = "http://api.openweathermap.org/data/2.5/weather?appid=9777aeb5531c2d51d999a49783fb454d&q=" #uses authentication key after appid, add left open with = to allow user to enter any location
    location = input("Enter weather location: ") #user input for location
    url = webadd+location #takes the add and appid for weather map and adds the location to make complete add
    data = requests.get(url).json()
    weather_description = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    temp2 = round((temp - 273.15),2) #converting kelvin to celcius
    speed = data["wind"]["speed"]
    
############# END OF IMPORTED CODE   

    value = False
    while value == False: #validation for when user gives wrong input- loop until valid
        if choice in range(1,4): #checks input is in range from 1 to 5 
            if choice == 1:
                print("The temperature in",location,"currently is",temp2,"celcius") # displays temperature
                value = True #appropriate input given so condition no longer false
            elif choice == 2:
                print("The weather in",location,"now is:",weather_description) #displays weatherdescription only of location (from all data)
                value = True
            elif choice == 3:
                print("The wind speed in",location,"is",speed,"mph")
                value = True
        else:
            choice = int(input("What you would like to see from the numbered options: "))
            value = False 
                                              
def AskForWeather():
    listofoptions = ["1: Temperature","2: Description","3: Wind"]
    sentence = input("What would you like to know? ").lower() #won't need to worry about case sensitivty 
    listofwords = sentence.split() #splits input sentence into list
    for word in listofwords:
        if word == "weather":
            print("Loading weather...")
            print()
            print(listofoptions)
            print()
            #choice = int(input("What you would like to see from the numbered options: "))
            WeatherConditions() #runs user input and validation
        else:
            continue 

AskForWeather()
