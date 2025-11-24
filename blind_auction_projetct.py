print("""
        _______
       /       \
      |  ____   |
      | |    |  |
       \|____|_/
           ||
===========||>>>
           ||
      -------------
      |           |
      |___________|

""")

def check_player_winner(game_players):
    highest_bid = 0
    highest_bid_key = ""
    
    for player in game_players:
        if game_players[player] > highest_bid:
            highest_bid_key = player
            highest_bid = game_players[player]
    
    print(f"The winner is {highest_bid_key} with a bid of {highest_bid}.")

game_finish = False
game_players = {}

print("Welcome to the secret auction program.")

while not game_finish:
    key = input("What is your name?: ")
    value = int(input("What's your bid?: $"))

    game_players[key] = value
    continue_bid = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    
    if continue_bid != "yes":
        game_finish = True
    
    print("\n * 100")

check_player_winner(game_players)
