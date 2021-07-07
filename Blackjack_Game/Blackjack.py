import random
from blackjack_art import logo
from IPython.display import clear_output

def compare_score():
    player_score = sum(player_cards)
    computer_score = sum(computer_cards)
    if computer_score == 21:
        print('You Lose, opponent has Blackjack 😱')            
    elif player_score == 21:
        print('You have a Blackjack, You win 😎') 
    elif player_score == computer_score:
        print('Match Draw 🙃')
    elif player_score > 21:
        print(f'You went over. You lose 😭')            
    elif computer_score > 21:
        print('Opponent went over. You win 😁')
    elif player_score > computer_score:
        print('You win 😃')
    else:
        print('You lose 😤')

def initial_check():
    player_score = sum(player_cards)
    computer_score = sum(computer_cards)
    print(f'    Your cards: {player_cards}, current score: {sum(player_cards)}')
    print(f'    Computer\'s first card: {computer_cards[0]}\n')
    if player_score >= 21 or computer_score >= 21:
        compare_score()
    else:
        blackjack()

def blackjack():
    '''This function is the brain of game'''
    if input("Type 'y' to get another card, type 'n' to pass: ").lower() == 'y':
        card_pick = random.choice(list_of_cards)
        if (sum(player_cards)+card_pick) >=21 and card_pick == 11:
            player_cards.append(1)
        else:
            player_cards.append(card_pick)
        if sum(computer_cards) <= 17:
            card_pick = random.choice(list_of_cards)
            if (sum(computer_cards)+card_pick) >=21 and card_pick == 11:
                computer_cards.append(1)
            else:
                computer_cards.append(card_pick)
        initial_check()
        
    else:
        while sum(computer_cards) <= 17:
            card_pick = random.choice(list_of_cards)
            if (sum(computer_cards)+card_pick) >=21 and card_pick == 11:
                computer_cards.append(1)
            else:
                computer_cards.append(card_pick)
        compare_score()
        return

while input("Do you want to play a game of Blackjack. Type 'y' or 'n': ").lower() == 'y':   
    clear_output(wait=True)
    print(logo)
    list_of_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_cards = random.choices(list_of_cards, k=2)
    computer_cards = random.choices(list_of_cards, k=2)
    initial_check()
    print(f"\n    Your final hand: {player_cards}, final score: {sum(player_cards)}")
    print(f"    Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
