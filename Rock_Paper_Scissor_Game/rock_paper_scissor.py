rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
game_list = [rock,paper,scissors]
choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors.\n'))
if choice not in [0,1,2]:
  print('Please enter correct choice')
else:
  user_choice = game_list[choice]
  print('You Chose: \n'+user_choice)
  auto_choice = random.choice(game_list)
  print('Computer chose:\n'+auto_choice)
  if (user_choice==rock and auto_choice==paper) or (user_choice==paper and auto_choice==scissors) or (user_choice==scissors and auto_choice==rock):
      print('You Lose.')
  elif user_choice==auto_choice:
      print('Game Tie')
  else:
      print('You Won.')
