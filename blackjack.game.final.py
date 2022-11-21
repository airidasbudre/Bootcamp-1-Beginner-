############### Our Blackjack House Rules #####################

 
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

import random
import os

def random_cards():
    """Return random card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    new_card_randomly = random.choice(cards)
    return new_card_randomly


def game():
    """Game logic"""
    player_cards = []
    computer_cards = []
    if start_of_game == "n":
        print("See you later")
    if start_of_game == "y":

    #Player first cards
        player_card = random_cards()
        player_cards.append(player_card)
        player_card = random_cards()
        score = sum(player_cards)
        if player_card == 11 and score > 10:
            player_card = 1
        player_cards.append(player_card)
        score = sum(player_cards)

     #Computer first cards
        computer_card = random_cards()
        computer_cards.append(computer_card)
        computer_card = random_cards()
        score_computer = sum(computer_cards)
        if computer_card == 11 and score_computer > 10:
            computer_card = 1
        computer_cards.append(computer_card)
        score_computer = sum(computer_cards)

        print(f"Your cards are {player_cards}, your score is {score}.")
        print(f"Computer first card is {computer_cards[0]}. ")
        
   
    #Second part(take more cards?)
    game_continue = True
    while game_continue == True:
        if score > 21:
            game_continue = False
        else:
            another_card = input("Do you wanna get another card? y or n: ")
            if another_card == "y":
                player_card = random_cards()
                if player_card == 11 and score > 10:
                    player_card = 1
                player_cards.append(player_card)
                score = sum(player_cards)
                print(f"Your cards are {player_cards}, your score is {score}.")
            if another_card == "n":
                game_continue = False

    #Computer turn
    computer_game_continue = True
    while computer_game_continue == True: 
        if score >= 21:
            computer_game_continue = False
        else: 
            while score_computer < 16:
                computer_card = random_cards()
                if computer_card == 11 and score_computer > 10:
                    computer_card = 1
                computer_cards.append(computer_card)
                score_computer = sum(computer_cards)
            computer_game_continue = False    

    print(f"Computer cards are {computer_cards}, computer score is {score_computer}")


    if score > 21:
        print("You lose")
    elif score_computer > 21:
        print("You win!")
    elif score == score_computer:
        print("It's draw!")
    elif score > score_computer:
        print("You win!")
    elif score < score_computer:
        print("You lose")  
#First part(first cards revealed)
start_of_game = input("Do you want to play game blackJack? y or n: ")
game_on = True
while game_on == True:
    if start_of_game == "n":
        print("See you later")
        game_on = False
    if start_of_game == "y":
        game()
        if game_on == True:   
            another_game = input("Do you want to play one more? y or n: ")
            if another_game == "y":
                os.system('cls')      
            else:
                game_on = False
                print("good bye")