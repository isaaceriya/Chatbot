import discord
import asyncio
import requests
from discord import Game
from discord.ext import commands


bot = commands.Bot(command_prefix='!')
 
# Welcoming new users to the server
@bot.event   
async def on_member_join(member):
    msg = 'Welcome ' + str(member.mention)
    await bot.send_message(discord.Object(id='506461145494978562'), msg)

#Change bot status on discord
@bot.event
async def on_ready():
    await bot.change_presence(game=Game(name="with Python"))
  

@bot.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == bot.user:
        return
    # Greets users who write hello
    if message.content.lower().startswith('hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await bot.send_message(message.channel, msg)
        
    # Counts how many messages a user has said    
    if message.content.lower().startswith('!count'):
        counter = 0
        tmp = await bot.send_message(message.channel, 'Calculating messages...')
        async for log in bot.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1
        await bot.edit_message(tmp, 'You have {} messages'.format(counter))
        
    # Weather integration    
    elif message.content.lower().startswith('!weather'):
        #import ChatBotWeather
        webadd = "http://api.openweathermap.org/data/2.5/weather?appid=9777aeb5531c2d51d999a49783fb454d&q="  
        await bot.send_message(message.channel, '''Choose a number from the options: 
        1: Temperature
        2: Description
        3: Wind''')
        choice = await bot.wait_for_message()
        choice = choice.content
        if choice == "1" or choice == "Temperature".lower():
            await bot.send_message(message.channel, "Enter weather location: ")
            location = await bot.wait_for_message()
            location = location.content
            url = webadd+location #takes the add and appid for weather map and adds the location to make complete add
            data = requests.get(url).json()
            weather_description = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            temp2 = str(round((temp - 273.15),2)) #converting kelvin to celcius
            speed = data["wind"]["speed"]
            msg = "The temperature in "+location+" currently is "+temp2+" celcius."
            await bot.send_message(message.channel, msg)
            
        if choice == "2" or choice == "Description".lower():
            await bot.send_message(message.channel, "Enter weather location: ")
            location = await bot.wait_for_message()
            location = location.content
            url = webadd+location #takes the add and appid for weather map and adds the location to make complete add
            data = requests.get(url).json()
            weather_description = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            temp2 = str(round((temp - 273.15),2)) #converting kelvin to celcius
            speed = data["wind"]["speed"]
            msg = "The weather in " +location +" now is: " +weather_description
            await bot.send_message(message.channel, msg)
            
        if choice == "3" or choice == "Wind".lower():
            await bot.send_message(message.channel, "Enter weather location: ")
            location = await bot.wait_for_message()
            location = location.content
            url = webadd+location #takes the add and appid for weather map and adds the location to make complete add
            data = requests.get(url).json()
            weather_description = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            temp2 = str(round((temp - 273.15),2)) #converting kelvin to celcius
            speed = str(data["wind"]["speed"])
            msg = "The wind speed in "+location+" is "+speed+" mph"
            await bot.send_message(message.channel, msg)
        
               
    # Time integration
    elif message.content.lower().startswith('!time'):        
        import time_finder
        await bot.send_message(message.channel, "The time is " + time_finder.currentTime())
        
    # Date integration    
    elif message.content.lower().startswith('!date'):
        import time_finder
        await bot.send_message(message.channel, "Today is " + time_finder.currentDate())
        
    elif message.content.lower().startswith('!calander'):
        import quickstart
        quickstart.main()
        
    elif message.content.lower().startswith('!music'):
        import Music
        
        
    # Shows available commands when writing a wrong command    
    elif message.content.lower().startswith('!'):
        msg = '''The available commands are: 
        !count
        !weather
        !time
        !date'''
        await bot.send_message(message.channel, msg)
                     
                      
            
            

bot.run("NTA2NDU5NzAyNDk4OTUxMTY5.DrifJg.H-hNsQUDYwBckwYE3VwczcTOWxA")
