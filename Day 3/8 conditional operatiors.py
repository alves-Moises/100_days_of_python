print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("what is your age? "))
    if age < 12:
        bill = 5
        print('Child pay $5.')
    elif age <= 18:
        bill = 7
        print("Youth pay $7.")
    elif age <= 45 and age > 55:
        bill = 0
        print("Free.")
    else:
        bill = 12
        print("Adult pay $12.")

    whants_phoyo = input("Do you want to take a photo waken?Y or N.")
    if whants_phoyo == "Y":
        bill += 3

    print(f"Your final bill is {bill}")

else:
    print("Sorry, you have to grouw up taller before you can ride.")