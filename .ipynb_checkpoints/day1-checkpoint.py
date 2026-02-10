# user_msg = input("Enter your messgae : ").lower()
# greet_msgs = ["hi","hello","hey","hi there","hello there"]
# if user_msg == "hi" or user_msg == "hello" or user_msg == "hey":
#     print("hell0")
# else:
#     print("I cannt understand")

greet_msgs = ["hi","hello","hey","hi there","hello there"]
chat = True
while chat:
    user_msg = input("Enter your messgae : ").lower()
    if user_msg in greet_msgs:
        print("hell0")
    elif user_msg =="bye":
        print("bye")
        chat = False
    else:
        print("I cannt understand")