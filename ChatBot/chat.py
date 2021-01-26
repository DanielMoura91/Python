from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

chatbot = ChatBot('Charlie')
trainer = ListTrainer(chatbot)
trainer.train(['Oi',
               'Olá',
               'Olá',
               'Oli',
               'Tudo bem?',
               'Tudo, e com você?',
               'Estou bem',
               'Que bom', ])

while True:
    user = input('Digite algo: ')
    bot = chatbot.get_response(user)
    print(bot)
