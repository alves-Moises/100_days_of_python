# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bisext = bool(((year % 4 == 0) if not(year % 100 == 0) else year % 400 == 0 ))

print(bisext)