from game_data import data
import random
import os


number1 = 0
number2 = 0
follower_count1 = 0
follower_count2 = 0
data_copy = []

def random_pick():
    global data_copy
    global data
    data_copy = data
    random_choice_1 = random.choice(data_copy)
    name = random_choice_1['name']
    global follower_count1
    follower_count1 = random_choice_1['follower_count']
    description = random_choice_1['description']
    country = random_choice_1['country']
    print(f" Compare A: {name}, {description}, from {country}")
    data_copy.remove(random_choice_1)
    
    random_choice_2 = random.choice(data_copy)
    name2 = random_choice_2['name']
    global follower_count2
    follower_count2 = random_choice_2['follower_count']
    description2 = random_choice_2['description']
    country2 = random_choice_2['country']
    print(f" Against B: {name2}, {description2}, from {country2}")
    

# if random_pick_1() == random_pick_2():
    


score = 0
game = True
while game == True:
    # Clearing the Screen
    os.system('cls')
    print(f"Your score is {score}.")
    random_pick()
    decision = input("Who have more followers? A or B: ")
    if follower_count1 > follower_count2:
        if decision == 'A':
            score += 1
        else:
            game = False 
            print("You are wrong. Game over.") 
    elif follower_count1 < follower_count2:
        if decision == 'B':
            score += 1
            print(f"Your score is {score}.")
        else:
            game = False
            print("You are wrong. Game over.") 