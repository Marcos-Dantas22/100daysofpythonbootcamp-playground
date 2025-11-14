import random

letters = [
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = [
    '!','@','#','$','%','&','*','-'
]

# Criar password com range(0, nr_letters + nr_numbers + nr_symbols)
# Adicionar num indice random os numbers randoms

print("Welcome to the PyPassword Generator")
nr_letters = int(input("How many letters would you like in your password\n"))
nr_symbols = int(input("How many symbols would you like\n"))
nr_numbers = int(input("How many numbers would you like\n"))

password = []

print(random.choice(letters, k=nr_letters))
password.append(random.choice(letters, k=nr_letters))
password.append(random.choice(numbers, k=nr_numbers))
password.append(random.choice(symbols, k=nr_symbols))
print(password)