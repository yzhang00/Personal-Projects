import random

comp_throw = random.choice(["rock", "paper", "scissors"])
while True:
    user_throw = input("Rock, paper, scissors, shoot!: ")
    print("The computer chose:", comp_throw)
    if user_throw == "rock":
        if comp_throw == "rock":
            print("Tie! Go again.")
        elif comp_throw == "paper":
            print("You lose!")
            break
        else:
            print("You win!")
            break
    elif user_throw == "paper":
        if comp_throw == "rock":
            print("You win!")
            break
        elif comp_throw == "paper":
            print("Tie! Go again.")
        else:
            print("You lose!")
            break
    elif user_throw == "scissors":
        if comp_throw == "rock":
            print("You lose!")
            break
        elif comp_throw == "paper":
            print("You win!")
            break
        else:
            print("Tie! Go again.")
    else:
        print("Please enter \"rock\", \"paper\", or \"scissors\".")
