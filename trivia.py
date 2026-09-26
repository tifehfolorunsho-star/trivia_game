
question1 = {
    "question": "What is the capital of france",
    "options": ["London","Paris","Madrid","Rome"],
    "answer": "paris"
}
question2 = {
    "question": "what is the capital of nigeria",
    "options": ["lagos","abuja","ikeja","ogun"],
    "answer": "abuja"
}
question3 = {
    "question": "what is the capital of kenya", 
    "options": ["nairobi","mombasa","kisumu","nakuru"],
    "answer": "nairobi"
}
question4 = {
    "question": "what is the capital of ghana", 
    "options": ["accra","kumasi","tamale","takoradi"],
    "answer": "accra"
}
question5 = {
    "question": "what is the capital of south africa",
    "options": ["cape town","pretoria","bloemfontein","durban"],
    "answer": "pretoria"
}
question6 = {
    "question": "the largest desert in the world is",
    "options": ["sahara","gobi","arabian","karakum"],
    "answer": "sahara"
}
question7 = {
    "question": "what is the largest mammal in the world",
    "options": ["african elephant","blue whale","giraffe","hippopotamus"],
    "answer": "blue whale"
}
question8 = {
    "question": "what is the largest ocean in the world",
    "options": ["pacific","atlantic","indian","arctic"],
    "answer": "pacific"
}
question9 = {
    "question": "what is the largest country in the world", 
    "options": ["china","russia","canada","usa"],
    "answer": "russia"
}
question10 = {
    "question": "what is the largest continent in the world",
    "options": ["asia","africa","north america","south america"],
    "answer": "asia"
}

questions = [
    question1,
    question2,
    question3,
    question4,
    question5,
    question6,
    question7,
    question8,
    question9,
    question10
]
letters = ["a","b","c","d"]
score = 0
for question in questions:
    print(question["question"])
    for letter, option in zip (letters,question["options"]):
        print(letter + ".",option)
    while True:
        answer = input("your answer:")
        if answer.lower() in letters:
            break
        print("Please choose A, B, C, or D.")
    selected_option = None
    for letter, option in zip (letters,question["options"]):
        if letter.lower() == answer.lower():
            selected_option = option
    
    if selected_option.lower() == question["answer"].lower():
        print("correct")
        score = score + 1
    else:
        print("wrong")
        print ("the correct answer is:",question["answer"])
print("your final score:",score,"out of",len(questions))
 
