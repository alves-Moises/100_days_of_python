# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

first = int(str((name1.lower().count('t') + name1.lower().count('r') + name1.lower().count('u') + name1.lower().count('e')) + (name2.lower().count('t') + name2.lower().count('r') + name2.lower().count('u') + name2.lower().count('e') ) ) + str((name1.lower().count('l') + name1.lower().count('o') + name1.lower().count('v') + name1.lower().count('e')) + (name2.lower().count('l') + name2.lower().count('o') + name2.lower().count('v') + name2.lower().count('e') ) ) )

print(f"Your score is {first}, you go together like coke and mentos."  if (first < 10 or first > 90) else f"Your score is {first}, you are alright together." if (first >= 40 and first <= 50) else f"Your score is {first}.") 