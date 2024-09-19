from words import word_list
import random
from hangman_art import hangman_logo,hangman_stages

random_word = random.choice(word_list)
length = len(random_word)
lives = 0

placeholder = ""
print(hangman_logo)
print(placeholder)

game_over = False
brain = []

for letter in random_word:
    placeholder += "_"


while not game_over:

    print(f"you have used {lives}\\6")

    guess = input("Guess the character: ").lower()

    if guess in brain:
        print("you have already guessed this letter")

    display = ""

    for letter in random_word:
        if letter == guess:
            display+=guess
            brain.append(guess)
        elif letter in brain:
            display += letter
        else:
            display+="_"
            
    print( "word to guess:" + display)


    if guess not in random_word:
        lives+=1
        if lives == 6:
            game_over = True
            print(f"You lose\n the word is {random_word}")


    if display == random_word:
        game_over = True
        print("game over you won")

    print(hangman_stages[lives])

    


