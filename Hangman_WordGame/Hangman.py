import random
from hangman_art import logo,stages
from hangman_words import word_list
from IPython.display import clear_output

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
guess_list=[]
lives = 6
print(logo)
print(f'sssh, the chosen word is {chosen_word}')

display = []
for blanks in range(word_length):
    display.append('_ ')

while not end_of_game:
    
    guess = input('Guess a letter: ').lower()
    clear_output(wait=True)
    
    if guess in guess_list:
        print(f'You have already guessed {guess}. Please choose a different letter')
        
    else:
        guess_list.append(guess)
        
        for index in range(word_length):
            if chosen_word[index] == guess:
                display[index] = chosen_word[index]
        if guess not in chosen_word:
            print(f'{guess} is not in chosen word. You lose a life')
            lives-=1
            if lives == 0:
                end_of_game = True
                print('You lose')
    print(''.join(display))
            
    if "_ " not in display:
        end_of_game = True
        print("You win.")
    
    print(stages[lives])    
