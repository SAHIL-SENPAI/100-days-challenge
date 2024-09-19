from game_data import data
from art import logo,vs
import random

print(logo)
score = 0


def compare(user_guess, a_count , b_count):
    if a_count > b_count:
        return user_guess == "a"
    else:
        return user_guess == "b"

def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"

    #genrating random account from game data

account_b = random.choice(data)


program_over = False
while not program_over:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"compare A: {format_data(account_a)}")
    print(vs)
    print(f"against B: {format_data(account_b)}")

    guess = input("who has more followers? 'A' or 'B': ").lower()

    print("\n"*20)

    #get follower of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    #compare funtion call
    is_correct = compare(guess,a_follower_count,b_follower_count)

    if is_correct == True:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        program_over = True
        print(f"Sorry, that's wrong. Final score: {score}")
