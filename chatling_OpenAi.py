from flask import Flask, render_template, request
import openai

app = Flask(__name__)

FORBIDDEN_WORDS = ['globglob']  # Add your forbidden words here
# Check for forbidden words in user_text

# Create a chatbot using OpenAI API
openai.api_key = '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'

def get_chatbot_response(user_text):
    response = openai.ChatCompletion.create(
        #model="gpt-3.5-turbo", # good
        #engine='text-davinci-003',  # or 'davinci' for chat models
        #engine='davinci-instruct-beta',  # for hebrew. gpt-3.5-turbo gives error openai.error.InvalidRequestError: This is a chat model and not supported in the v1/completions endpoint. Did you mean to use v1/chat/completions?
        #engine="chatGPT",  # GPT-4 model openai.error.InvalidRequestError: The model `chatGPT` does not exist
        #engine="davinci",  # GPT-3 model, very low quality answers
        model = "gpt-3.5-turbo-16k",
        messages=[
            #{"role": "system", "content": "You are a helpful assistant."},
            {"role": "system", "content": "please answer focused answers, not more than 30 words, you are history teacher and You know everything about Winston Churchill. Please do not answer any topic not related to Winston Churchill,be nice and funny if you can."},
            {"role": "user", "content": user_text}
        ]
    )
    return response.choices[0].message.content.strip()

# Create database for logging and chat conversation history


@app.route("/")
def home():
    return render_template("index_openai_api.html")


@app.route("/get", methods=['GET'])
def get_bot_response():
    user_text = request.args.get('msg')
    
    for word in FORBIDDEN_WORDS:
        if word in user_text:
            return "Sorry, I cannot process your request."

    bot_response = get_chatbot_response(user_text)
    return bot_response


if __name__ == "__main__":
    app.run(debug=False)
