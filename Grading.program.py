student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for grade in student_scores:
    if (student_scores[grade]) >= 91:
       student_grades[grade] = "Outstanding" 
    elif  91 > (student_scores[grade]) >= 81:
       student_grades[grade] = "Exceeds expectations"
    elif  81 > (student_scores[grade]) >= 71:
       student_grades[grade] = "Acceptible"
    elif  (student_scores[grade]) < 70:
       student_grades[grade] = "Fail"
    print(grade)
    
    

# 🚨 Don't change the code below 👇
print(student_grades)