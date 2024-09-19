print('''⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⣿⣿⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣰⣿⣿⣿⡿⠁⡀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⣿⣿⣿⡟⢀⣼⣿⣶⣤⣀⠘⠿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣼⣿⣿⣿⠟⢀⣾⣿⣿⣿⣿⣿⣷⣦⣄⠉⠻⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣾⣿⣿⣿⠏⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⠻⢿⡿⠃⠰⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠆⢠⣿⣷⣦⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⣠⣿⣿⣿⡟⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢴⣦⣄⠙⠻⣿⣿⣿⣿⣿⣿⡿⠃⣰⣿⣿⣿⡟⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣈⠙⠻⣶⠄⠉⠛⠿⣿⡿⠁⣼⣿⣿⣿⠟⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⠏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠛⢿⣿⣿⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣾⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠛⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')

print("Welcome to the silent bidding...")


bidding_log = {}
program_over = False

while not program_over:
    name = input("Enter your name: ")
    bid  = int(input("Enter the bid amount: $"))

    bidding_log[name] = bid

    is_over = input("are there any other bidder? enter 'yes' or 'no'").lower()
    if is_over == 'no':
        program_over = True
    else:
        print("\n"*100)


def find_highest_bidder(bidding_dictonary):
    highest_bid = 0
    winner = ''
    for bidder in bidding_dictonary:
        bid_amount = bidding_dictonary[bidder]
        if bid_amount>highest_bid:
            highest_bid = bid_amount
            winner = bidder.upper()

    
    print(f"Winner is {winner} with the bid amount of ${highest_bid}")


find_highest_bidder(bidding_log)





