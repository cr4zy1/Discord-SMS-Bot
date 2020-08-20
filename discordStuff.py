import sys
import discord
from mailer import send_email
from email_csv_utils import *
from config import token
import signal
import sys

names = []

def signal_handler (sig,frame):
    print("SIGINT NIBBA")
    sys.exit(0)

def messageSplitter(msg, amount):
    msg = msg[amount:] # removes the '$sms '
    data = msg.split('|')
    data[0] = data[0].strip()
    data[1] = data[1].strip()
    return data


client = discord.Client()
@client.event
async def on_ready():
    print("Logon Successful")#logon to discord using token


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$sms'):
        if message.content == "$sms help" or message.content == "$sms h" : # help menu
            await message.channel.send("Help:\nTo send a message use \"$sms send {CONTACT NAME} | {MESSAGE}\" or \"$sms s {CONTACT NAME} , {MESSAGE}\"\nTo add a contact to the database, use \"$sms add {NAME} | {EMAIL}\" or \"$sms a {NAME} | {EMAIL}\"\nTo delete a contact from the database use \"$sms delete {Contact Name}\" or \"$sms d {contact name}\"\nTo view the contact list, use \"$sms list\" or \"$sms l\" \nThe contact must be listed as name and email. ex - xxxyyyzzzz@carrier.com ")
        if message.content.startswith("$sms send") or  message.content.startswith("$sms s"): #send message
            if message.content.startswith("$sms send"):
                adder = messageSplitter(message.content, 10)
                PN = getEmail(adder[0])
                if(send_email("",adder[1],PN)):                
                    await message.channel.send("Message Sent")
                else:
                    await message.channel.send("Invalid Message")
            else:
                adder = messageSplitter(message.content, 7)
                PN = getEmail(adder[0].strip())
                if(send_email("",adder[1],PN)):                
                    await message.channel.send("Message Sent")
                else:
                    await message.channel.send("Invalid Message")
                    
        if message.content.startswith("$sms add") or message.content.startswith("$sms a"): # add to contacts
            if message.content.startswith("$sms add"):
                adder = messageSplitter(message.content, 8)
                nameFile.append(adder)
                await message.channel.send(adder[0] + " added to database")
            else:
                adder = messageSplitter(message.content, 6)
                nameFile.append(adder)
                await message.channel.send(adder[0] + " added to database")
            writeDatabase(nameFile)
                
        if message.content.startswith("$sms delete") or message.content.startswith("$sms d"): #remove from contacts
            if message.content.startswith("$sms delete"):
                remover = message.content[12:]
                a=0
                for i in nameFile:
                    if(i[0] == remover):
                        nameFile.pop(a)
                        print(i[0] + "removed")
                    a+=1
            else:
                remover = message.content[7:]
                a=0
                for i in nameFile:
                    if(i[0] == remover):
                        nameFile.pop(a)
                        print(i[0] + " removed")
                    a+=1
            writeDatabase(nameFile)

            
        if message.content.startswith("$sms list") or message.content.startswith("$sms l"): #view the database
            printer = ""
            for i in nameFile:
                if(i[0] != "name"):
                    printer=printer + i[0] + "\n"
                

            await message.channel.send(printer)

nameFile = getDatabase()
client.run(token)#run the code
