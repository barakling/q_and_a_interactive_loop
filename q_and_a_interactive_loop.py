from transformers import pipeline
import time

start_time = time.time() 

try:
    # Initialize a QA pipeline
    qa_pipeline = pipeline("question-answering", model = "bert-large-uncased-whole-word-masking-finetuned-squad")
    #full success bert-large-uncased-whole-word-masking-finetuned-squad
    #success without hard: distilbert-base-cased-distilled-squad 
    #no success: xlnet-large-cased, google/electra-large-discriminator

    # Context information
    context = r"""
    The Johnson family is an ordinary family living in Seattle. The family consists of five members. 

    The father, Robert, is a software engineer who enjoys cycling during his free time. He is 40 years old. Robert is known for his pancakes that he cooks every Sunday morning for breakfast. 

    The mother, Emily, is a school teacher who is passionate about painting and often exhibits her work at local galleries. Emily is 37 years old and her favorite book is "Pride and Prejudice".

    Their oldest son, Mike, is a high school student and an avid basketball player. At the age of 17, he already stands at 6 feet 2 inches tall and her favorite book is "the bla and the blee".

    Their second son, Sam, is 14 years old. Sam is very interested in robotics and spends much of his free time building models with his robotics kit. He recently won first place in a school-wide science fair for a robot he designed and built himself.

    Finally, their daughter, Lucy, is the youngest in the family at 10 years old. Lucy loves to play piano and often gives mini concerts for her family in the living room. Her favorite song to play is "Fur Elise" by Beethoven.
    """
    #question = "what robert enjoys?" #easy question
    #question = "which book is the favorite of Emily?" #easy question
    #question = "which book is the favorite of Mike?" #harder question
    #question = "What does Robert do for a living?" # hard question
    #question = "where is the sun?" # impossible question
    #question = "What is Robert's financial situation?" # impossible question
    
    end_time = time.time()  # Get the current time again

    while True:  # Keep the program running until the user decides to quit
            question = input("Please enter your question (or 'bye' to exit): ")

            if question.lower() == 'bye':
                break

            start_time = time.time() 

            # Get a prediction from the QA model
            prediction = qa_pipeline(question=question, context=context)

            end_time = time.time()  # Get the current time again
            elapsed_time = end_time - start_time  # Compute the difference

            # Check if the model returned an answer
            if prediction['answer']:
                print(f"\nQuestion: {question}")
                # Check prediction score and modify answer accordingly
                if prediction['score'] < 0.6:
                    print(f"Answer: I'm not sure, but I think {prediction['answer']}, score: {prediction['score']}, start: {prediction['start']}, end: {prediction['end']}")
                else:
                    print(f"Answer: {prediction['answer']}, score: {prediction['score']}, start: {prediction['start']}, end: {prediction['end']}")
            else:
                print("Sorry, I don't know the answer for that, but I promise I'll study it soon.")
            print(f'The question was processed in: {elapsed_time:.2f} seconds')

except Exception as e:
    print(f"We apologize, an error occurred: {e}")
