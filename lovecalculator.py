print("Love calculator")
me = input("Write your full name: ")
lover = input("Write his or her full name: ")

us = me + lover
print(us)

us_lower = us.lower()

t1 = us_lower.count('t')
r1 = us_lower.count("r")
u1 = us_lower.count("u")
e1 = us_lower.count("e")

true = t1 + r1 + u1 + e1

l1 = us_lower.count("l")
o1 = us_lower.count("o")
v1 = us_lower.count("v")
e11 = us_lower.count("e")

love = l1 + o1 + v1 + e11 

score = str(true) + str(love)
score2 = int(score)

if score2 < 10 or score2 > 90:
    print(f"Your score is {score}. You go together like coke and mentos")
elif 40 >= score2 <= 50:
     print(f"Your score is {score2}. You alright together")
else:
    print(f"Score: {score2}")
