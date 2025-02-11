# Dictionary of questions and answers
# randomly pick the question
# Ask the user question and take answer as input
# Keep track of the score
# Tell the score to the user

import random

qa_dict = {
    "What is the capital of France?": "Paris",
    "Who wrote 'To Kill a Mockingbird'?": "Harper Lee",
    "What is the square root of 64?": "8",
    "Who developed the theory of relativity?": "Albert Einstein",
    "What is the chemical symbol for gold?": "Au",
    "How many continents are there on Earth?": "7",
    "What is the largest planet in our solar system?": "Jupiter",
    "Who painted the Mona Lisa?": "Leonardo da Vinci",
    "What is the longest river in the world?": "The Nile River",
    "What year did World War II end?": "1945"
}

def trivia_game():
    questions_list = list(qa_dict.keys())
    total_questions = 5
    score = 0

    selected_questions = random.sample(questions_list, total_questions)
    for index, question in enumerate(selected_questions):
        print(f"{index}. {question}")
        correct_answer = qa_dict[question]
        user_answer = input("Your answer: ").lower()
        
        if user_answer == correct_answer.lower():
            print("Correct\n")
            score += 1
        else:
            print(f"Wrong, correct answer is {correct_answer}.")

    print(f"you got correct {score}/{total_questions}")

trivia_game()
