print("welcome to the Pizza Deliveries")

size = input("What size of pizza you want to order? S(Small), M(Medium), L(Large): ")
bill = 0

if size == "S":
    print("Small cost $15")
    bill += 15
elif size == "M":
    print("Medium cost $20")
    bill += 20
else:
    print("Large cost $25")
    bill += 25

pepperoni = input("Do you want extra pepperoni? Y or N? ")

if pepperoni == "Y":
    if size == "S":
        bill = bill + 2
    else:
        bill = bill + 3

cheese = input("Do you want extra cheese? Y or N? ")

if cheese == "Y" or "y":
    bill = bill + 1
    print("Your final bill: ", bill)
else:
    print("Your final bill: ", bill)
