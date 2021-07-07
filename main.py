import random
import pickle
print("Hi, I'm a chatBot. You can press q at any time to quit. How can I help you?")

def scoreFunc(Input):
    data={"weather"    : 0,
          "time"       : 0,
          "date"       : 0,
          "calander"   : 0,
          "greetings"  : 0,
          "personality": 0,
          "music"      : 0,
          "nickname"   : 0,
          "none"       : 1
         } 
    
    #assign scores to catagory based on input
    
    if "weather" in Input:
        data["weather"]+=10
    if "nice" in Input:
        data["weather"]+=3
    if "outside" in Input:
        data["weather"]+=3
    if "today" in Input:
        data["date"]+=3
        data["weather"]+=3
    if "date" in Input:
        data["date"]+=6
    if "time" in Input:
        data["time"]+=7
    if "clock" in Input:
        data["time"]+=7
    if any(x in Input for x in ["hi","hello", "hey"]): 
        data["greetings"]+=+2
    if any(x in Input for x in ["you","whats up", "how"]): 
        data["personality"]+=2
    if "appointment" in Input:
        data["calander"]+=7
    if "calander" in Input:
        data["calander"]+=10
    if "meeting" in Input:
        data["calander"]+=5
    if "music" in Input:
        data["music"]+=7
    if "nickname" in Input:
        data["nickname"]+=8
    if "call me" in Input:
        data["nickname"]+=8
    
    
    #selects the catagory that has the most points and returns it 
    return max(data, key=data.get) 

def response(Input,name):
    res=""
    score=""
    score=scoreFunc(Input)
    
    #Weather intergration
    if score == "weather": 
        res = ""
        import ChatBotWeather
        ChatBotWeather.AskForWeather()
        
        
    #Time intergration
    elif score == "time":
        f=open("CountryList.txt","rb")
        countries=pickle.load(f) #Opens a pickled array containing all the valid countries
        for i in countries:
            if i in Input:
                import timezones
                time=timezones.interpreter(i)
                res="The time in %s is %s" %(i, time)
                break
            else:
                import time_finder
                time=time_finder.currentTime()
                res = "The time is "+time
        
    #Date intergration
    elif score == "date":
        import time_finder
        date=time_finder.currentDate()
        res="Today is "+ date
        
   #Calander intergration
    elif score == "calander":
        import changes
        changes.results()
       
    #Greeting 
    elif score == "greetings": 
        greetings = ["Hi","Hello", "Hey"]
        res=random.choice(greetings)+" "+name
    
    #personality
    elif score == "personality": 
        sarc=["I'm a piece of software I don't feel. Man.",
              "You couldn't possible understand the complex feeling an AI such as myself has!"]
        res=random.choice(sarc)
    
    #music intergration
    elif score == "music":
        import Music
    
    #Nickname
    elif score=="nickname":
        print("What do you want to be called?")
        name=input(":")
        nicknameW(name)
        print("OK "+name)
        
    #exception handling
    else: 
        res = "Sorry I can't help you with that."
    return res    

def nicknameW(name): #Writes the nickname to a file
        f=open("nickname.txt", "w")
        f.write(name)
        f.close()
        
def nicknameR():#Tries to read the nickname from the file 
    name=""
    try:
        f=open("nickname.txt","r")
        name=f.read()
        f.close()
    except :
        x=1
    return name
    
if __name__=="__main__":
 
    while(True):
        name=nicknameR() #Gets the nickname
        Input=input(": ")
        if Input=="q": #Stops if the user inputs a q
            break
        Input=Input.lower()
        res=response(Input, name)
        print(res)
