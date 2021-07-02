import string
from caesar_art import logo
print(logo)
alphabet = list(string.ascii_lowercase)
run_again = 'yes'

def caesar(start_text, shift_code, direc):
    output=''
    shifted_alphabet = alphabet[shift_code:]+alphabet[:shift_code]
    for letter in start_text:
        if letter in alphabet:
            if direc == 'encode':
                index = alphabet.index(letter)
                output += shifted_alphabet[index]
            elif direc == 'decode':
                index = shifted_alphabet.index(letter)
                output += alphabet[index]
        else:
            output += letter        
    print(f'The {direc}d text is {output}') 

while run_again == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction == 'encode' or direction == 'decode':
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))%26
        caesar(text, shift, direction)
        run_again = input('Do you want to restart? Type "Yes" or "No".').lower()
    else:
        print('Please enter correct direction.Try again.')
print('GoodBye')
