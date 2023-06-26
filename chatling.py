from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
#from collections.abc import Hashable


app = Flask(__name__)

# Create a chatbot instance
chatbot = ChatBot("My Chatbot")

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on the Hebrew corpus
trainer.train("chatterbot.corpus.hebrew")

# Train the chatbot on additional corpus files
trainer.train(r"venv\Lib\site-packages\chatterbot_corpus\data\hebrew\botprofile.yml")
#trainer.train(r"venv\Lib\site-packages\chatterbot_corpus\data\hebrew\conversations.yml")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    response = str(chatbot.get_response(user_text))
    return response

if __name__ == "__main__":
    app.run(debug=False)