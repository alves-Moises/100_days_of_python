from re import S


student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.

student_grades = dict()

#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    student_grades[student] = 'Fail' if (student_scores[student] <= 70) else 'Acceptable' if (student_scores[student] <=  80) else "Exceeds Expectations" if (student_scores[student] <= 90) else "Outstanding"

    

# 🚨 Don't change the code below 👇
print(student_grades)
