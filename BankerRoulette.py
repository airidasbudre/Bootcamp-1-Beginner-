import random

list1 = []


people = input("Write all names: ")
group_of_people = people.split(",")

list2 = list1.extend(group_of_people)

a = str(random.random(group_of_people))

print(f"For food should pay {a}")
