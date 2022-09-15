

height = input("Write all students height: ").split()

number_of_students = 0
height_sum = 0

for i in height:
    number_of_students = number_of_students + 1
    height_sum = height_sum + int(i)
print(height_sum/number_of_students)