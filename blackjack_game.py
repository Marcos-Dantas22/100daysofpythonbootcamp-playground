import random

print("""

.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      '------'                           |__/ 
		
""")
game_finish = False

def get_cards(number_cards, cards_list):
    cards_available = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    
    for card in range(0, number_cards):
        cards_list.append(random.choice(cards_available))
    
    if 11 in  card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)
    
    return cards_list

while not game_finish:
    player_cards = []
    computer_cards = []
    
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    game_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    
    if game_choice == "y":
        player_cards = get_cards(2, player_cards)
        computer_cards = get_cards(1, computer_cards)
        
        print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
        print(f"Computer's first card: {computer_cards}")
                            
        while True:
            get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            
            if get_another_card == "y":
                player_cards = get_cards(1, player_cards)                
                print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
                print(f"Computer's first card: {computer_cards}")
                
                if sum(player_cards) > 21:
                    break
            else:
                break
        
        if sum(computer_cards) <= 15:
            while True:
                computer_cards = get_cards(1, computer_cards)
                
                if sum(computer_cards) >= 16:
                    break
            
        print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
        print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
        
        if sum(player_cards) > 21:
            print("You went over. You lose")
        elif sum(computer_cards) > 21:
            print("Opponent went over. You win")
        
        elif sum(player_cards) - 21 == sum(computer_cards) - 21:
            print("Draw Game")
        elif sum(player_cards) - 21 > sum(computer_cards) - 21:
            if sum(player_cards) == 21 and len(player_cards) == 2:
                print("Win with a Blackjack!")
            else:
                print("You win")
        elif sum(computer_cards) - 21 > sum(player_cards) - 21:
            if sum(computer_cards) == 21 and len(computer_cards) == 2:
                print("Lose with a Blackjack")
            else:
                print("You lose")
       
    else:
        game_finish = True
	
