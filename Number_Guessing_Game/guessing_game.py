from random import randint
from number_guess import logo

ATTEMPTS_EASY = 10
ATTEMPTS_HARD = 5

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        return ATTEMPTS_EASY
    elif difficulty == 'hard':
        return ATTEMPTS_HARD
    else:
        print('Please enter correct diffficulty.')

def check_answer(player_guess, computer_guess, attempts):
    
    """checks answer against guess. Returns the number of turns remaining."""
    if player_guess > computer_guess:
        print('Too High.')
        return attempts - 1
    elif player_guess < computer_guess:
        print('Too Low.')
        return attempts - 1
    else:
        print(f'You got it! The answer was {computer_guess}')        
        
def game():
    print(logo)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    computer_guess = randint(1,100)
    print(f'sssh, the correct answer is {computer_guess}')
    attempts = set_difficulty()
    player_guess = 0
    while player_guess != computer_guess:
        print(f"You have {attempts} attempts remaining to guess the number.")
        player_guess = int(input('Make a guess: '))
        attempts = check_answer(player_guess, computer_guess, attempts)
        if attempts == 0:
            print('You have run out of guesses, you lose.')
            return
        elif player_guess != computer_guess:
            print('Guess Again.')
game()
