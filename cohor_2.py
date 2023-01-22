import discord
import cohere
import os
from cohor import convo
import json


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def save_prompt(prompt:str):
    with open('prompt.txt', 'w') as f:
        f.write(prompt)

def load_prompt():
    try:
        with open('prompt.txt', 'r') as f:
            return f.read()
    except:
        return ""

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    Intial_prompt = load_prompt()
    if message.author == client.user:
        return
    else:
        new_prompt = f"""
    --
    patient: {message.content}
    """
        Intial_prompt = Intial_prompt+new_prompt
        res = convo(Intial_prompt)
        Intial_prompt = Intial_prompt+res
        print(Intial_prompt)
        save_prompt(Intial_prompt)
        await message.channel.send(res)



client.run('MTA2NjI0MDY4NzA1OTc2NzM3Ng.GoGIEL.LPNUdXT_0uw6gg6kVUfnx2XpquvvlfkDaocQVw')