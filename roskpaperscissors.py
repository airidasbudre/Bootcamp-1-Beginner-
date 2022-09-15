from random import randint
import random

rock = 'o' 
paper = '-<>'
scissors = '><'

game_options = [rock, paper, scissors]

#player choose the option
player = int(input("Choose your option - 0 rock, 1 paper, 2 scissors: "))
player_desicion = game_options[player]
print(player_desicion)

#computer gets random option
computer = int(random.randint(0,2))
computer_desicion = game_options[computer]
print(computer_desicion)


#Check who wins

if player_desicion == computer_desicion:
    print("Equal! Play once again.")
elif player_desicion == 'o' and computer_desicion == '-<>' or player_desicion == '-<>' and computer_desicion == '><' or player_desicion == '><' and computer_desicion == 'o' :
    print("Computer wins!")
else:
    print('Player wins!')

