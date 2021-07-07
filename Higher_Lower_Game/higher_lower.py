from game_data import data
from high_low_art import logo, vs
from IPython.display import clear_output
import random

print(logo)
first_choice = random.choice(data)
second_choice = {}
score = 0


def game(first_choice,second_choice,score):
    second_choice = random.choice(data)
    while first_choice == second_choice:
        second_choice = random.choice(data)
    print(f"Compare A: {first_choice['name']}, a {first_choice['description']}, from {first_choice['country']}.")
    print(vs)
    print(f"Against B: {second_choice['name']}, a {second_choice['description']}, from {second_choice['country']}.")
    
    if input("Who has more followers? Type 'A' or 'B': ").lower() == 'a':    
        player_guess = first_choice['follower_count']
    else:
        player_guess = second_choice['follower_count']

    max_followers = max(first_choice['follower_count'],second_choice['follower_count'])
    clear_output(wait=True)
    print(logo)
    if player_guess == max_followers:
        score += 1
        print(f"You're right! Current score: {score}.")
        game(first_choice = second_choice,second_choice={}, score = score)
    else:
        print(f"Sorry, that's wrong. Final Score: {score}.")
game(first_choice,second_choice,score)
