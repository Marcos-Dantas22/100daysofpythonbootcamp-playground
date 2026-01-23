import random

print("""
/ _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ' _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|        
""")

def generate_random_number():
    return random.randint(1,100)
        
def check_number_correct(number_correct, answer):
    if answer > number_correct:
        print("Too high.")
        return False
    elif answer < number_correct:
        print("Too low.")
        return False
    else:
        print(f"You got it! The answer was {number_correct}.")
        return False
                  

game_finish = False

while not game_finish:
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_correct = int(generate_random_number())
    answer = input("Choose a difficulty. Type 'easy' or 'hard': ")
    
    if answer == "easy":
        count = 10
    elif answer == "hard":
        count = 5
    else:
        break
    
    
    while count > 0:
        print(f"You have {count} attempts remaining to guess the number.")

        answer_number = int(input("Make a guess: "))
        check = check_number_correct(number_correct, answer_number)
        
        if check is True:
            game_finish = True
            break
        
        print("Guess again.")
        count-=1
    
    print("You've run out of guesses. Refresh the page to run again.")
    game_finish = True
        
    	