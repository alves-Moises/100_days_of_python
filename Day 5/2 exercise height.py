# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total, i = 0, 0
for n in range(0, len(student_heights)):
    total += student_heights[n]
    i+= 1

print(f'average: {round(total/i)}')