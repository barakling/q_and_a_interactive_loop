from flask import Flask, request
from transformers import pipeline

app = Flask(__name__)

# Initialize the QA pipeline outside of the route so it doesn't get reloaded each time.
qa_pipeline = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")

# Context information
context = r"""
The Johnson family is an ordinary family living in Seattle. The family consists of five members. 
The father, Robert, is a software engineer who enjoys cycling during his free time. He is 40 years old. Robert is known for his pancakes that he cooks every Sunday morning for breakfast. 
The mother, Emily, is a school teacher who is passionate about painting and often exhibits her work at local galleries. Emily is 37 years old and her favorite book is "Pride and Prejudice".
Their oldest son, Mike, is a high school student and an avid basketball player. At the age of 17, he already stands at 6 feet 2 inches tall and her favorite book is "the bla and the blee".
Their second son, Sam, is 14 years old. Sam is very interested in robotics and spends much of his free time building models with his robotics kit. He recently won first place in a school-wide science fair for a robot he designed and built himself.
Finally, their daughter, Lucy, is the youngest in the family at 10 years old. Lucy loves to play piano and often gives mini concerts for her family in the living room. Her favorite song to play is "Fur Elise" by Beethoven.
"""

@app.route('/ask', methods=['POST'])
def ask():
    try:
        question = request.json['question']

        # Get a prediction from the QA model
        prediction = qa_pipeline(question=question, context=context)

        # Check if the model returned an answer
        if prediction['answer']:
            # Check prediction score and modify answer accordingly
            if prediction['score'] < 0.6:
                return {
                    "question": question,
                    "answer": f"I'm not sure, but I think {prediction['answer']}",
                    "score": prediction['score'],
                    "start": prediction['start'],
                    "end": prediction['end']
                }
            else:
                return {
                    "question": question,
                    "answer": prediction['answer'],
                    "score": prediction['score'],
                    "start": prediction['start'],
                    "end": prediction['end']
                }
        else:
            return {"message": "Sorry, I don't know the answer for that, but I promise I'll study it soon."}

    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    app.run(port=5000, debug=True)
