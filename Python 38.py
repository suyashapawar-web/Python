import random

option = input("Choose rock, paper or scissors.")
option.lower()
choices = ["scissors", "rock", "paper"]
r_choices = random.choice(choices)
print("The computer chose:",r_choices)
if r_choices == option:
    print("Draw!")
elif r_choices == "rock" and option == "paper":
    print("You win!")
elif r_choices == "scissors" and option == "rock":
    print("You win!")
elif r_choices == "paper" and option == "scissors":
    print("You win!")
else:
    print("Computer wins!")

if option not in ["rock", "paper", "scissors"]:
    print("Please pick either rock, paper or scissors!")

