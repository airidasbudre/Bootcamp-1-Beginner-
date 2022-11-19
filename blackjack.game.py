############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

import random

def random_cards():
    """Return random card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    new_card_randomly = random.choice(cards)
    return new_card_randomly

start_of_game = input("Do you want to play game blackJack? y or n:")

if start_of_game == "n":
   print("See you later")
if start_of_game == "y":
   first_player_card = random_cards()
   second_player_card = random_cards()
   print(f"Your cards are [{first_player_card}, {second_player_card}], your score is {")