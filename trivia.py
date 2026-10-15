import random
questions = [
    {
        "question": "What is the capital of france",
        "options": ["London","Paris","Madrid","Rome"],
        "answer": "paris"
    },
    {
        "question": "what is the capital of nigeria",
        "options": ["lagos","abuja","ikeja","ogun"],
        "answer": "abuja"
    },
    {
        "question": "what is the capital of kenya",
        "options": ["nairobi","mombasa","kisumu","nakuru"],
        "answer": "nairobi"
    },
    {
        "question": "what is the capital of ghana",
        "options": ["accra","kumasi","tamale","takoradi"],
        "answer": "accra"
    },
    {
        "question": "what is the capital of south africa",
        "options": ["cape town","pretoria","bloemfontein","durban"],
        "answer": "pretoria"
    },
    {
        "question": "the largest desert in the world is",
        "options": ["sahara","gobi","arabian","karakum"],
        "answer": "sahara"
    },
    {
        "question": "what is the largest mammal in the world",
        "options": ["african elephant","blue whale","giraffe","hippopotamus"],
        "answer": "blue whale"
    },
    {
        "question": "what is the largest ocean in the world",
        "options": ["pacific","atlantic","indian","arctic"],
        "answer": "pacific"
    },
    {
        "question": "what is the largest country in the world",
        "options": ["china","russia","canada","usa"],
        "answer": "russia"
    },
    {
        "question": "what is the largest continent in the world",
        "options": ["asia","africa","north america","south america"],
        "answer": "asia"
    }
]   
    

# questions = [
#     question1,
#     question2,
#     question3,
#     question4,
#     question5,
#     question6,
#     question7,
#     question8,
#     question9,
#     question10
# ]
letters = ["a","b","c","d"]

   
while True:
    score = 0
    while True:
        try:
            number_of_questions = int(input("how many questions do you want to answer (1-10)?:"))  
            if 1 <= number_of_questions <= len(questions):
                break
            else:
                print("Please enter a number between 1 and", len(questions))
        except ValueError:
            print("Please enter a valid number.")
            continue
    selected_questions = random.sample(questions, number_of_questions)
    for selected_question in selected_questions:
        print(selected_question["question"])
        for letter, option in zip (letters,selected_question["options"]):
            print(letter + ".",option)
        while True:

            answer = input("your answer:")
            if answer.lower() in letters:
                break
            print("Please choose A, B, C, or D.")
        selected_option = None
        for letter, option in zip (letters,selected_question["options"]):
            if letter.lower() == answer.lower():
                selected_option = option
        if selected_option.lower() == selected_question["answer"].lower():
            print("correct")
            score = score + 1
        else:
            print("wrong")
            print ("the correct answer is:",selected_question["answer"])
    print("your final score:",score,"out of",(number_of_questions))
    continue_choice = input("Do you want to play again? (y/n):")
    if continue_choice.lower() != "y":
        break
    