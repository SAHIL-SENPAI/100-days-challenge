import random
from hangman_art import hangman_stages , hangman_logo

from words import word_list

print(hangman_logo)
random_word = random.choice(word_list)
lives = 0

random_word_size = len(random_word)
placeholder = ""
for i in range(random_word_size):
    placeholder += "_"

print(placeholder)

game_over = False
brain = []

while not game_over:
    print(f"*********************{lives}/6 LIVES USED**************************")
    user_guess = input("Guess the character : ").lower()
    

    if user_guess in brain:
        print(f"you have already guessed{user_guess} , choose something else")


    display = ""
    for letter in random_word:
        if letter == user_guess:
            display += letter
            brain.append(user_guess)
        elif letter in brain:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if user_guess not in random_word:
        lives += 1
        print(f"You guessed {user_guess}, thats not in the word. You lose a life.")
        if lives == 6:
            game_over = True
            print(f"*************************it was {random_word}, YOU LOSE*************************")




    if "_" not in display:
        game_over = True
        print("**************************YOU WON*************************")

    print(hangman_stages[lives])

