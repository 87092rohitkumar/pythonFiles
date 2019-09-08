from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
#from chatterbot.trainers import ChatterBotCorpusTrainer
import os

bot = ChatBot('Bot')
#bot.set_trainer(ListTrainer)

#for files in os.listdir('/home/roshan/testpython/venv/lib/python3.7/site-packages/chatterbot_corpus/data/english/'):
#	data = open('/home/roshan/testpython/venv/lib/python3.7/site-packages/chatterbot_corpus/data/english/' + files , 'r').readlines()
#	bot.train(data)
	#trainer = ListTrainer(data)

conv = open('chats.txt' , 'r')
bot.train(conv)
while True:
	message = input('You:')
	reply = bot.get_response(message)
	print('ChatBot:',reply)
	if message.strip() == 'Bye':
		print('ChatBot: Bye')
		break
		
