import discord
import cohere
import os
from cohor import convo
import json
from cohere_convo_2 import convo_2

from gmaps_api import GoogleMapsClient




GOOGLE_API_KEY = 'AIzaSyBdPwSklxcsSD-QaExwKkCp2CgkxpHcoQU'


with open("log.txt", "w") as f:
    f.truncate()


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def save_prompt(prompt:str,filename_1):
    with open(filename_1, 'w') as j:
        j.write(prompt)
    j.close()


def load_prompt(file_name):
    with open(file_name, 'r', encoding='cp1252', errors='ignore') as f:
        string_ = f.read()
        return string_

Intial_prompt = load_prompt('Intial_prompt.txt')
save_prompt(Intial_prompt,'prompt.txt')

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
res_last= ""
mess_last=""
counter = 0



@client.event
async def on_message(message):
    global res_last
    global mess_last
    if message.content.startswith('!clear'):
        Intial_prompt = load_prompt('Intial_prompt.txt')
        save_prompt(Intial_prompt,'prompt.txt')
        return 
    global counter
    if message.author != client.user:
        counter += 1
    print(counter)
    
    if counter == 6:
        with open('log.txt', 'r', encoding='cp1252', errors='ignore') as f:
            log_contents = f.read()
            log_contents = log_contents.split("\n")
            log_contents = [x for x in log_contents if x.strip() != '']
            seriousness = convo_2(log_contents)
            if seriousness == "no emergency":
                print("no emergency")
                res_tempt = convo("Please create a respones to end a conversation due of a non emergency support line ")
                counter = 0
                await message.channel.send(res_tempt)

            if seriousness == "emergency":
                print("emergency")
                string_help = "Can you please provide me with the following pieces of information that you're comfortable sharing with me, such as:  Age, Location, Field of study, GPA, Gender"
                counter = 7
                await message.channel.send(string_help)


    if counter==7:
        location = convo("Analyis the following message and extract location from it:"+"\n" + message.content)
        print(location)
        USER_ADRESS = location
        USER_PLACE = 'Mental health'

        client_gmaps = GoogleMapsClient(api_key=GOOGLE_API_KEY, address=USER_ADRESS)

        testing = client_gmaps.search(keyword=USER_PLACE, radius=60000)['results']

        potential_places = []
        dummy = []
        for i in range(len(testing)):
            potential_places.append(testing[i]['name'])
            dummy.append(testing[i]['place_id'])
        output_gmaps = f"Based off the information you provided, the nearest facility where you can receive help is {potential_places[0]}"
        await message.channel.send(output_gmaps)


    Intial_prompt = load_prompt('prompt.txt')
    

    if message.author == client.user:
        return
    else:
        new_prompt = f"""
--
patient: {message.content}
"""
        Intial_prompt = Intial_prompt+new_prompt
        
        res = convo(Intial_prompt)
        previous_res = ""
        i=0
        while (res == previous_res) and i<4:
            res = convo(Intial_prompt)
            i+=1
            if i==4:
                await message.channel.send("I dont Think I can help out")
                return 
        previous_res = res
        Intial_prompt = Intial_prompt+res

        save_prompt(Intial_prompt,'prompt.txt')
        save_prompt(mess_last,'log.txt')
        mess_last = mess_last +"\n"+  message.content 
        res_last = res+res_last
        await message.channel.send(res.split(':', 1)[-1])



client.run('MTA2NjI0MDY4NzA1OTc2NzM3Ng.GoGIEL.LPNUdXT_0uw6gg6kVUfnx2XpquvvlfkDaocQVw')