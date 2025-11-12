print("Welcome to Python Pizza deliveries!")
size = input("What size pizza do you want, S, M or L:")
pepperoni = input("Do you want pepperoni on your pizza? Y or N:")
extra_cheese = input("Do you want extra cheese? Y or N:")

value = 0

if size == "S":
	value += 15
elif size == "M":
	value += 20
elif size == "L":
	value += 25
	
if pepperoni == "Y" and size == "S":
	value += 2

if pepperoni == "Y" and (size == "L" or size == "M"):
	value += 3
	
if extra_cheese == "Y":
	value += 1;
	
print(f"Your final bill is: ${value}") 

