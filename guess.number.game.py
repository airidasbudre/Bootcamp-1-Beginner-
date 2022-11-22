import random


print("Welcome to the game guess the number!")
print("You have to find number beetween 1 and 100 by guessing.")
difficulty = input("Choose the difuculty. 'easy' or 'hard': ")
attemts = None
random_number_1 = None

if difficulty == 'easy':
   attemts = 10
elif difficulty == 'hard':
    attemts = 5

random_number_1 = random.randint(1, 100)
right_aswer = False
while right_aswer == False:
    if  attemts > 0:
        print(f"You have {attemts} attemts left")
        guess = int(input("Guess the number: "))
        attemts -= 1
        if random_number_1 > guess:
            print("Too low")
        elif random_number_1 < guess:
            print("Too high")
        elif random_number_1 == guess:
            print(f"You are right. The answer is {random_number_1}")
            right_aswer = True
    else:
        right_aswer = True
