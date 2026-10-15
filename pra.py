# class number:
#     def _iter_ (self):
#         set = 1
#         return self
#     def next (self):
#         x = set
#         set += 1
#         return x
# date = number()
# first = iter(date)
# print(next(first))


# try:
#     number_of_questions = int(input("how many questions do you want to answer?"))
#     if number_of_questions <= 0:
#         print("Please enter a positive number.")
#     elif number_of_questions > len(questions):
#         print("Please enter a number less than or equal to", len(questions))
#     else:
#         selected_questions = random.sample(questions, number_of_questions)
#         for selected_question in selected_questions:
#             print(selected_question["question"])
#             for letter, option in zip (letters,selected_question["options"]):
#                 print(letter + ".",option)
#             while True:
#                 answer = input("your answer:")
#                 if answer.lower() in letters:
#                     break
#                 print("Please choose A, B, C, or D.")
#             selected_option = None
#             for letter, option in zip (letters,selected_question["options"]):
#                 if letter.lower() == answer.lower():
#                     selected_option = option

#             if selected_option.lower() == selected_question["answer"].lower():
#                 print("correct")
#                 score = score + 1
#             else:
#                 print("wrong")
#                 print ("the correct answer is:",selected_question["answer"])
#         print("your final score:",score,"out of",(number_of_questions))

# age = int(input("enter your age:"))
# if age >= 18:
#     print("You are an adult")
# if age <= 18:
#     print("you are a minor")

#
# password = input("enter a password:")
# data = "python123"
# if password == data:
#     print("access granted")
# else:
#     print("access denied")

age = int(input("enter your age:"))
if age >= 18:
     print("You are an adult")
#     if age >= 65:
#         print("You are a senior citizen")
else:
     print("You are a minor")
# total = 0
# for number in range(1,11):
#     sum = 5
#     total = number * sum

#     print (sum, "*",number, "=", total)