print("""

		   _____________________
		  /  _________________  \
		 /  /                 \  \
		|  |  >>>  python  <<<  | |
		|  |  _________________|  |
		|  | | 7 | 8 | 9 | ÷ | |  |
		|  | |---+---+---+---| |  |
		|  | | 4 | 5 | 6 | × | |  |
		|  | |---+---+---+---| |  |
		|  | | 1 | 2 | 3 | - | |  |
		|  | |---+---+---+---| |  |
		|  | | 0 | . | = | + | |  |
		|  | |___|___|___|___| |  |
		|  |___________________|  |
		 \_______________________/
				\  /    \  /
				 \/      \/
				  \  /\  /
				   \/  \/
					\  /
					 \/
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
           _/\_     _/\_     _/\_    
          ( o o)   ( o o)   ( o o)
          /  V  \  /  V  \  /  V  \
         /--===--\/--===--\/--===--\
        /  pythonista calculator!   \
        \___________________________/
		
""")
game_finish = False
continue_calculation = False

def add(f_number, n_number):
	return f_number + n_number
def sub(f_number, n_number):
	return f_number - n_number
def multiplication(f_number, n_number):
	return f_number * n_number
def division(f_number, n_number):
	return f_number / n_number

operations = {
	"+": add,
	"-": sub,
	"*": multiplication,
	"/": division,
}

while not game_finish:
	
	if not continue_calculation:
		f_number = float(input("What's the first number?: "))
	
	print("+, -, *, /")
	operation = input("Pick an operation: ")
	n_number = float(input("What's the next number?: "))
	
	print(operation in operations)
	if operation in operations:
		total = operations[operation](f_number, n_number)
	else:
		print("Operation typed is not a option valid!")
		game_finish = True
		continue
		
	print(f"{f_number} {operation} {n_number} = {total}")
	check_continue_calculation = input(f"Type 'y' to continue calculing with {total}, or type 'n' to start a new calculation: ")
	
	if check_continue_calculation == "y":
		f_number = total
		continue_calculation = True
	elif check_continue_calculation == "n":
		continue_calculation = False
	else:
		print("Option typed is not a option valid!")
		game_finish = True