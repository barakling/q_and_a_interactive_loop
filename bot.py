#https://realpython.com/build-a-chatbot-python-chatterbot/
'''PS> python -m venv venv
PS> venv\Scripts\activate
(venv) PS> python -m pip install chatterbot==1.0.4 pytz'''

# bot.py

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from cleaner import clean_corpus

CORPUS_FILE = "chat.txt"

chatbot = ChatBot("Chatpot")

trainer = ListTrainer(chatbot)
cleaned_corpus = clean_corpus(CORPUS_FILE)
trainer.train(cleaned_corpus)

trainer.train([
    "Hi",
    "Welcome, dear friend 🤗",
])
trainer.train([
    "Hello",
    "Hello to you too",
])
trainer.train([
    "Hey",
    "Hey dear friend, How can I help you?",
])
trainer.train([
    "How are you?",
    "I'm good, tnx for asking, how are you?",
])
trainer.train([
    "i'm good",
    "good to hear that, How can I help you?",
])
trainer.train([
    "good",
    "good to hear that, How can I help you?",
])
trainer.train([
    "הי",
    "הי, איך אוכל לעזור?",
])

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")