print('''  _                                       _     _                 _ 
| |_ _ __ ___  __ _ ___ _   _ _ __ ___  (_)___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ | / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ | \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___| |_|___/_|\__,_|_| |_|\__,_| ''')

print("Welcome to treasure island !!")
choice = input("you can choose to go left or right to continue you journey, which one do you choose?").lower()
if choice == "left":
    print("congrats you arrived at a sea sore safely")
    choice2 = input('''you can "wait" for you crew or "go" for the treasure''').lower()

    if choice2 == "wait":
        #continue
        print("your crew is arrived , and you'all reached to the one peice ")
        choice3 = input("you opened the treasre and there are three doors in fornt of you , RED , YELLOW ans BLUE choose one to get your treasure").lower()
        
        if choice3 == "yellow":
            print("CONGRATS PIRET , ONE PEICE IS YOURS")
        else:
            print("GAME OVER")
    else:
        print("game over, you've been eaten by sarks")



else:
    print("you lost in the desert , game over")
    