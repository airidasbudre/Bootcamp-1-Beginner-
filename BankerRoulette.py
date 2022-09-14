import random


people = input("Write all names: ")
group_of_people = people.split(",")

number = len(group_of_people)

a = random.randint(0, number)

c = group_of_people[a]


print(f"For food should pay {c}")
