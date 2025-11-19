import random

stages = [
""" 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
""" 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
""" 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
""" 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
""" 
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
""" 
  +---+
  |   |
      |
      |
      |
      |
=========
"""
]


word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = "_" * len(chosen_word)

print("_" * len(chosen_word))

finish_game = False
lives = 6

correct_words = []


while not finish_game:
	print(f"********************<???> {lives} LIVES LEFT********************") 
	guess = input("Guess a letter: ").lower()
	display = ""
	
	if guess in correct_words:
		print("You already guessed this word")
	
	for letter in chosen_word:
		if letter == guess:
			display += letter
			correct_words.append(letter)
		elif letter in correct_words:
			display += letter
		else:
			display += "_"
			
	if guess not in correct_words:
		print(f"You guessed {guess}, thats not in the word, You lose a life")
		lives-=1
		print(stages[lives])
	
		if lives == 0:
			print("********************YOU LOSE********************")
			finish_game = True
	
	if not "_" in display:
		finish_game = True
		print("********************YOU WIN********************")
	
	print(display)