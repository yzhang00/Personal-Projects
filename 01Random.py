import random

com_num = random.randrange(0, 21, 1)
user_num = -1
while user_num != com_num:
    user_num = int(input("Guess a number: "))
    if user_num > com_num:
        print("Too high.")
    elif user_num < com_num:
        print("Too low.")
print("You got it! The number was:", com_num)