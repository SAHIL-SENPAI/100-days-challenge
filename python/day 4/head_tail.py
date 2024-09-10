import random
choice1 = ['head' , 'tail']
user_choice = input("choose head or tails").lower()
computer_choice = random.choice(choice1)

if user_choice == computer_choice:
    print(f"its {user_choice}, you won")
else:
    print("you lost")


