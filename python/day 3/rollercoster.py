print("Welcome to the rollercoster!")
height = int(input("enter your height in cm"))
age = int (input("enter your age : "))
bill = 0

if height>=120:
    if age<12:
        bill = 5
        print("you have to pay $5")
    elif age<18:
        bill = 7
        print("you have to pay $7")
    else:
        bill = 10
        print("you have to pay $10")

    user = input("do you want a photo? type y or n ")
    if user == "y":
        bill+=3
    
    print(f"final bill is ${bill}")

else:
    print("sorry, you cant ride")