for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        number = 'FizzBuzz'
        #print("Fizz")
    elif number % 5 == 0:
        number = 'Buzz'
        #print("Buzz")
    elif number % 3 == 0:
        number = 'Fizz'
        #print("FizzBuzz")
    print(number)