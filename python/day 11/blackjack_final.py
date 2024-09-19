import random
from blackjack_art import art

print(art)


#function to return a random card
def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

#addition of list items
def calculate_score(cards):
    #means user or computer hit blackjack and black jack is represented
    #by 0
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    

    #make the 11 into 1 if card sum exceeds 21 (note - this is a rule of blackjack)
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score,computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, oppenent has BlackJack"
    elif user_score == 0:
        return "Win with a BlackJack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"


def playgame():
    print('''
    .------.            _     _            _    _            _    
    |A_  _ |.          | |   | |          | |  (_)          | |   
    |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
    | \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
    |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
    '-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
        |  \/ K|                            _/ |                
        '------'                           |__/ 
    ''')
    user_cards = []
    computer_cards = []
    program_over = False
    #in case of error or loop skiping
    computer_score = -1 #we cant make this 0 cuz in our program that means blackjack
    user_score = -1


    #so we can have 2 card assigned for both user and computer
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    while not program_over:
    #sum of user and computer decks ;)
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, Current score: {user_score} ")
        print(f"Computer's first card is: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            program_over = True
        else:
            user_should_deal = input("Type 'y' to get another card or 'n' to pass: ").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                program_over = True


    #computers turn 
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score=user_score,computer_score=computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n"*30)
    playgame()