import random
from Hangman_pictures import a
from words import list_of_words
from os import system
from sys import platform

clear_screen = lambda: system("cls" if platform == "win32" else "clear")
clear_screen() # will clear the console

count_letter = -1
lives = 6
count_right_guess = 0
stages = 0

#Random word
random_word = random.choice(list_of_words)
print(random_word)

#Blank generation
lenth_of_word = len(random_word)
blanks1 = '_' * lenth_of_word 
blanks = list(blanks1)
print(blanks)

# Insert letter and Checking inserted letter
end_of_the_game = False
while not end_of_the_game:
      Input = input("Input your guess letter: ").lower()
      if Input in blanks:
        print('You already typeed this letter\n')

      # Checking if input matches with any letter  
      for i in random_word:
          count_letter += 1 
          if i == Input:
             blanks[count_letter] = i
             count_right_guess += 1 
      
      print(blanks)
      count_letter = -1   

# Declare when the game is finished
      if '_' not in blanks:
        print('you win')
        end_of_the_game = True
      if Input not in random_word:
         lives -= 1
         stages += 1
         print(a[stages])    
         if stages == 6:
             end_of_the_game = True
             print("You lost")
     