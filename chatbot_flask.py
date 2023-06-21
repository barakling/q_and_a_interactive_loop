from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

chatbot = ChatBot("Chatpot")

trainer = ListTrainer(chatbot)

# Add your training data here
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

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))

if __name__ == "__main__":
    app.run(debug=False)