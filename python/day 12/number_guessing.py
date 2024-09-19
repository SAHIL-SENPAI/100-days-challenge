from number_art import value
import random
print(value)

random_number = random.randint(1,100)

print("welcome to the number guessing game ! ")
print("im thinking of a number between 1 to 100, can you guess??")

difficulty = input("Choose the difficulty 'easy' or 'hard': ").lower()


attempts = 5
if difficulty == 'easy':
    attempts = 10


program_over = False

while not program_over:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Guess the number: "))
    if guess == random_number:
        print("RIGHT, You won")
    elif guess > random_number:
        print("TOO HIGH")
    elif guess < random_number:
        print("TOO LOW")
    else:
        print("invalid input")

    
    if random_number == guess:
        program_over = True
    
    attempts -= 1
    if attempts == 0 :
        program_over = True
        print(f"Out of attempts ,you loose , the number is {random_number}")
    

    
