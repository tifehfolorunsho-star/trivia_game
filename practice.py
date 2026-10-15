# import json
# def add():
#     while True:
#         try:
#             number = int(input("Enter a number:"))
#             if number >= 0:
#                 print(number)
#                 return number
#             else:
#                 print("non integer")
#         except:
#             print("invalid input")
# def save():
#     number = add()
#     with open("save.json","w") as file:
#         json.dump(number,file)
# save()
# def get():
#     name = "muftiat"
#     second = name[5]
#     print(second)
# get()
# # except ValueError:
#     print("invalid input")

# def square(number):
#     return number*number
# print(square(5))

# def multiply(a,b):c
#     return a*b
# print(multiply(4,7))

def check_number(number):
    if number%2 == 0:
        return "even"
    else:
        return "odd"
print(check_number(2))