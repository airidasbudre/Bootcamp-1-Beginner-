def prime_checker(number):
    count = 0
    for i in range(1,number + 1): 
        if number % i == 0:
            count += 1
    if count == 2:
        print("Prime number")
    else:
        print("Not prime number")
    
        


n = int(input("Input number: "))
prime_checker(number = n)