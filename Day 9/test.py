student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

student_grades = {}

for chaves in student_scores:
    if student_scores[chaves] > 90 and student_scores[chaves] <= 100:
        student_grades[chaves] = "Outstanding"
    elif student_scores[chaves] > 80 and student_scores[chaves] <= 90:
        student_grades[chaves] = "Exceeds Expectations"
    elif student_scores[chaves] > 70 and student_scores[chaves] <= 80:
        student_grades[chaves] = "Acceptable"
    elif student_scores[chaves] <= 70:
         student_grades[chaves] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)