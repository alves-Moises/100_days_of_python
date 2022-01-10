#pizza order

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


total = ( 16 if (size == 'S') else 20 if (size == 'M') else 25 ) + (0 if (add_pepperoni == False) else 2 if (size == 'S') else 3) + (1 if extra_cheese == 'Y' else 0)
print(f'Final bill is: {total}')