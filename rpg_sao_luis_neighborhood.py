print('''
 __________________________________________________________________________

.--------.  .--.  .--.  .--.   .--.  .--------.
| .-------\ | .-\ | .-\ | .-\  | .-\ | .-------\
| | .-----' | | | | | | | |  \ | | | | | .---._|
| | |  .-.  | | | | | | | |   `| | |  \| `-----.
| | |  |.-\ | | |_| | | | | \   \| | .-`-----. |
| | `---' | | | `---' | | | |`\  ` | | .-----' |
| |       | | |       | | | |  |\  | | |       |
 \|       |  \|       |  \| |   \| |  \|       |
  `-------'   `-------'   `-'    `-'   `-------'
''')

print("Welcome to Guns Game")
print("Your mission is escape for 'Coroadinho'")
print("A very dangerous neighborhood from São Luis Maranhão")

road = input("Choose you walk for a dirt road or paved road? D or P:")

if road == "D":
	print("You encountered a suspicious person and were hit by a gunshot. Game over")
elif road == "P"
	print("You arrived at a narrow street")
	narrow_street = input("with a wall around it, do you continue straight ahead or go back? S or B")
	if narrow_street == "B":
		print("You encountered a suspicious person and were hit by a gunshot. Game over")
	elif narrow_street == "S":
		print("You arrived at the entrance to Avenida dos Africanos")
		hide_or_go = input("but a motorcycle passed you and is coming back, do you hide from the motorcycle or go towards it? H or G")
		if hide_or_go == "G":
			print("You were an idiot and you were killed. Game over")
		elif hide_or_go == "H":
			print("You were smart and managed to get out of the neighborhood. You Win!") 
		else:
			print("You didn't enter any option")

	else:
		print("You didn't enter any option")
else:
	print("You didn't enter any option")
	
