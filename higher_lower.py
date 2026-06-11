import random

data = [
    {"name": "Cristiano Ronaldo", "follower_count": 635000000, "description": "Football player", "country": "Portugal"},
    {"name": "Lionel Messi", "follower_count": 505000000, "description": "Football player", "country": "Argentina"},
    {"name": "Selena Gomez", "follower_count": 430000000, "description": "Singer and actress", "country": "United States"},
    {"name": "Kylie Jenner", "follower_count": 400000000, "description": "Entrepreneur and influencer", "country": "United States"},
    {"name": "Dwayne Johnson", "follower_count": 395000000, "description": "Actor and former wrestler", "country": "United States"},
    {"name": "Ariana Grande", "follower_count": 380000000, "description": "Singer and actress", "country": "United States"},
    {"name": "Kim Kardashian", "follower_count": 365000000, "description": "Media personality and entrepreneur", "country": "United States"},
    {"name": "Beyoncé", "follower_count": 320000000, "description": "Singer and songwriter", "country": "United States"},
    {"name": "Khloé Kardashian", "follower_count": 305000000, "description": "Television personality", "country": "United States"},
    {"name": "Nike", "follower_count": 300000000, "description": "Sportswear brand", "country": "United States"},
    {"name": "Justin Bieber", "follower_count": 295000000, "description": "Singer", "country": "Canada"},
    {"name": "Kendall Jenner", "follower_count": 290000000, "description": "Model and entrepreneur", "country": "United States"},
    {"name": "Taylor Swift", "follower_count": 285000000, "description": "Singer-songwriter", "country": "United States"},
    {"name": "Virat Kohli", "follower_count": 270000000, "description": "Cricketer", "country": "India"},
    {"name": "Jennifer Lopez", "follower_count": 250000000, "description": "Singer and actress", "country": "United States"},
    {"name": "Neymar Jr", "follower_count": 225000000, "description": "Football player", "country": "Brazil"},
    {"name": "National Geographic", "follower_count": 215000000, "description": "Nature and science media", "country": "United States"},
    {"name": "Nicki Minaj", "follower_count": 230000000, "description": "Rapper and singer", "country": "Trinidad and Tobago"},
    {"name": "Miley Cyrus", "follower_count": 210000000, "description": "Singer and actress", "country": "United States"},
    {"name": "Katy Perry", "follower_count": 205000000, "description": "Singer and songwriter", "country": "United States"},
    {"name": "Zendaya", "follower_count": 190000000, "description": "Actress and singer", "country": "United States"},
    {"name": "Kevin Hart", "follower_count": 180000000, "description": "Comedian and actor", "country": "United States"},
    {"name": "Real Madrid", "follower_count": 175000000, "description": "Football club", "country": "Spain"},
    {"name": "FC Barcelona", "follower_count": 170000000, "description": "Football club", "country": "Spain"},
    {"name": "UEFA Champions League", "follower_count": 120000000, "description": "Football competition", "country": "Switzerland"},
    {"name": "Premier League", "follower_count": 80000000, "description": "Football league", "country": "England"},
    {"name": "NASA", "follower_count": 98000000, "description": "Space agency", "country": "United States"},
    {"name": "9GAG", "follower_count": 58000000, "description": "Entertainment platform", "country": "Hong Kong"},
    {"name": "ESPN", "follower_count": 52000000, "description": "Sports media company", "country": "United States"},
    {"name": "Marvel", "follower_count": 70000000, "description": "Entertainment company", "country": "United States"},
    {"name": "Netflix", "follower_count": 46000000, "description": "Streaming platform", "country": "United States"},
    {"name": "Disney", "follower_count": 39000000, "description": "Entertainment company", "country": "United States"},
    {"name": "FIFA", "follower_count": 50000000, "description": "Football organization", "country": "Switzerland"},
    {"name": "Shakira", "follower_count": 92000000, "description": "Singer and songwriter", "country": "Colombia"},
    {"name": "David Beckham", "follower_count": 89000000, "description": "Former football player", "country": "England"},
    {"name": "Shah Rukh Khan", "follower_count": 47000000, "description": "Actor and producer", "country": "India"},
    {"name": "Priyanka Chopra", "follower_count": 92000000, "description": "Actress and producer", "country": "India"},
    {"name": "Anitta", "follower_count": 65000000, "description": "Singer", "country": "Brazil"},
    {"name": "Whindersson Nunes", "follower_count": 60000000, "description": "Comedian and influencer", "country": "Brazil"},
    {"name": "Felipe Neto", "follower_count": 17000000, "description": "Content creator and entrepreneur", "country": "Brazil"},
    {"name": "MrBeast", "follower_count": 70000000, "description": "Content creator and philanthropist", "country": "United States"},
    {"name": "Mark Zuckerberg", "follower_count": 15000000, "description": "Technology entrepreneur", "country": "United States"},
    {"name": "Bill Gates", "follower_count": 12000000, "description": "Philanthropist and entrepreneur", "country": "United States"},
    {"name": "Elon Musk", "follower_count": 25000000, "description": "Entrepreneur and investor", "country": "United States"},
    {"name": "Linus Sebastian", "follower_count": 3000000, "description": "Technology content creator", "country": "Canada"},
    {"name": "Mosh Hamedani", "follower_count": 1200000, "description": "Programming educator", "country": "Canada"},
    {"name": "freeCodeCamp", "follower_count": 2500000, "description": "Programming education platform", "country": "United States"},
    {"name": "Python Learning", "follower_count": 850000, "description": "Python tutorials and tips", "country": "United States"},
    {"name": "Django Developers", "follower_count": 350000, "description": "Django web development content", "country": "United Kingdom"},
]

print(r"""
╔══════════════════════╗
║       HIGHER         ║
╚══════════════════════╝
           │
           ▼
        ┌─────┐
        │ VS  │
        └─────┘
           ▲
           │
╔══════════════════════╗
║       LOWER          ║
╚══════════════════════╝
""")

def get_account():
    return random.choice(data)
                 
game_finish = False
game_points  = 0

print("Welcome to the Higher Lower Game!")
while not game_finish:
	option = get_account()
	option2 = get_account()
	print(f"Compare A: {option['name']}, {option['description']} from {option['country']}") 
	print(r"""
	    ┌─────┐
        │  VS │
        └─────┘
	""")
	print(f"Against B: {option2['name']}, {option2['description']} from {option2['country']}")    
	answer = input("Who has more followers? Type 'A' or 'B': ")

	if option["follower_count"] > option2["follower_count"] and answer.upper() == "A":
		game_points+=1
		print(f"You're right!, Current Score: {game_points}")
	elif option2["follower_count"] > option["follower_count"] and answer.upper() == "B":
		game_points+=1
		print(f"You're right!, Current Score: {game_points}")
	else:
		print(f"Sorry, that's wrong. Final score: {game_points}")
		game_finish = True

	print("\n")
	

