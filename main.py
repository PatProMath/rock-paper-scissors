import random

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
game_images = [rock, paper, scissors]

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n")) # Never forgetting to wrap the input method in an int() method.

if player <= 2 and player >= 0:
  print(game_images[player])
else:
  print("No play!")

computer = random.randint(0,2)
print("Computer chose: \n")

print(game_images[computer])

# To check win
if player == computer:
  print("It's a draw")
elif (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
  print("You lose!🤖")
elif (player == 1 and computer == 0) or (player == 2 and computer == 1) or (player == 0 and computer == 2):
  print("You win! 😤🎉")
else:
  # Anticipating no play by player
  print("Assuming no play by player...😪 Computer wins🥱.")


"""
Line 29 replaces all of these...
def play(choice):
  if choice == 0:
    print(rock)
  elif choice == 1:
    print(paper)
  elif choice == 2:
    print(scissors)
  else:
    print("No play!")
    
# play(player_choice)
   
Previous Code I had in lines 34 - 37 and 42

# play(computer_choice)
if computer == 0:
  print(rock)
elif computer == 1:
  print(paper)
else:
  print(scissors)


"""