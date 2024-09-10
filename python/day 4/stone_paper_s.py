import random
your_choice = int(input("what do you choose? 0 for rock , 1 for paper , 2 for scissors"))
choices = ["rock" , "paper" , "scissors"]
computer_choice = random.choice(choices)

if choices[your_choice] == computer_choice:
    print(f"both choose {computer_choice}, DRAW")
elif choices[your_choice]=="rock":
    if computer_choice == "paper":
        print("computer won")
    else :
        print("you won")
elif choices[your_choice] == "paper":
    if computer_choice == "rock":
        print("you won")
    else:
        print("computer won")
elif choices[your_choice]=="scissors":
    if computer_choice == "rock":
        print("computer won")
    else:
        print("you won")
else:
    print("oops someting went wrong")