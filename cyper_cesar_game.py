print("""
   ____________________________
  |============================|
  |        CYPER CAESAR        |
  |----------------------------|
  |   An ancient cipher wheel  |
  |   used to shift letters    |
  |   and hide secret codes.   |
  |____________________________|
         \   ^   ^   ^   /
          \  |   |   |  /
           \ |   |   | /
            \|   |   |/
            (|---+---|)
            /|   |   |\
           / |   |   | \
          /  v   v   v  \
""")

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z'
]

def encrypt(original_text, shift_amount):
    text_shifted = ""
    for letter in original_text:
        if letter == ' ':
            text_shifted = text_shifted + letter
        else:
            index_letter = alphabet.index(letter)
            new_index = index_letter + shift_amount

            if new_index > 25:
                letter_aux = new_index - 25 - 1
                letter_shifted = alphabet[letter_aux]
            else:
                letter_shifted = alphabet[new_index]

            text_shifted = text_shifted + letter_shifted

    return text_shifted


def decrypt(original_text, shift_amount):
    text_decript = ""
    for letter in original_text:
        if letter == ' ':
            text_decript = text_decript + letter
        else:
            index_letter = alphabet.index(letter)
            new_index = index_letter - shift_amount
            letter_shifted = alphabet[new_index]
            text_decript = text_decript + letter_shifted

    return text_decript


game_finish = False

while not game_finish:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        text_encrypt = encrypt(text, shift)
        print(text_encrypt)
    elif direction == "decode":
        text_decript = decrypt(text, shift)
        print(text_decript)
    else:
        print("option not find")

    choice_finish_game = input("Type 'yes' to finish game, type 'no' to not finish:\n").lower()

    if choice_finish_game == "yes":
        game_finish = True
