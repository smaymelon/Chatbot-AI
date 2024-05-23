from chatterbot  import ChatBot
from chatterbot.trainers import ListTrainer
import webbrowser#lets the program open webbrowsers

bot = ChatBot('MyChatBot')
bot.set_trainer(ListTrainer)
 
conversation = open('AI.txt','r').readlines()
name= input("What is your name:")#this lets the user put in their name so you can speak to the bot
bot.train(conversation)

while True:
    message = input(name +": ")#puts the name of user and starts an input for anything they ask
    message = message.lower()#puts all messages into lower so it can funnel through
    if "?" in message:#if question has a ? it will open up google for them
        print(webbrowser.open_new("https://google.com"))
    if "image" in message:#if they want a picture it will open up google images for them
        print(webbrowser.open_new("https://www.google.com/imghp?hl=EN"))
    if message.strip()!= 'Bye':
     reply = bot.get_response(message)
    print('ChatBot:',reply)
    if message.strip()=='bye':#if user says bye it will end the program
        break
