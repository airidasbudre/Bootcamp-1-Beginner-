import random

number_of_letters = int(input("How many letters should be in your password? \n"))
number_of_symbols = int(input("How many symbols should be in your password? \n"))
number_of_numbers = int(input("How many numbers should be in your password? \n"))

letters_list = []
symbols_list = []
numbers_list = []

times1 = 0 
times2 = 0
times3 = 0

password = ''

list_of_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
'V', 'W', 'X', 'Y', 'Z']
list_of_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
list_of_symbols = ['!', '#', '?']


#list of letters   
for i in random.choices(list_of_letters, k=number_of_letters):
    if number_of_letters >= times1:
       times1 += 1
       letters_list.append(i)
print(letters_list)

#list of symbols
for i in random.choices(list_of_symbols, k=number_of_symbols):
    if number_of_symbols >= times2:
       times2 += 1
       symbols_list.append(i)
print(symbols_list)  

#list of numbers
for i in random.choices(list_of_numbers, k=number_of_numbers):
    if number_of_numbers >= times3:
       times3 += 1
       numbers_list.append(i)
print(numbers_list)  

#put all lists to the one
letters_list.extend(symbols_list)
letters_list.extend(numbers_list)

print(letters_list)
lenth_of_password = len(letters_list)

#Mix position

random.shuffle(letters_list)
print(letters_list)

#from list to string and 
for i in letters_list:
    password = password + str(i)   
print(password)
