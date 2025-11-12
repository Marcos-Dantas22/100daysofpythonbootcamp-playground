import random

print('''
 __________________________________________________________________________

===============================
   ROCK - PAPER - SCISSORS
           GAME
===============================

        ✊   🖐️   ✌️
''')

print("Welcome to Rock - Paper - Scissors Game")

choose = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

def show_choose_icon(choose):
	if choose == '0':
		print('''
			    _______
			---'   ____)
				  (_____)
				  (_____)
				  (____)
			---.__(___)
		''')
	elif choose == '1':
		print('''
			    _______
			---'   ____)____
					  ______)
					  _______)
					 _______)
			---.__________)
		''')
	else:
		print('''
			    _______
			---'   ____)____
					  ______)
				   __________)
				  (____)
			---.__(___)
		''')
		
if choose in ['0','1','2']:
	computer_choice = str(random.randint(0,2))
	show_choose_icon(choose)
	print("Computer choose: ")
	show_choose_icon(computer_choice)
	
	if choose == computer_choice:
		print("Draw game")
	elif choose == '0' and computer_choice == '2':
		print("You Won")
	elif choose == '1' and computer_choice == '0':
		print("You Won")
	elif choose == '2' and computer_choice == '1':
		print("You Won")
	else:
		print("You lose")

else:
	print("You didn't enter any option")