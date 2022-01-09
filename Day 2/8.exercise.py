#Tip Calculator
print("Welcome to the tip calculator!")
total = float(input("What was the total bill?"))
percent = float(input("What percentage top would you like to gie? 10, 12 or 15?"))
nPeople = int(input("How many people to split the bill?"))

print(f"Each person shoyd pay: ${((total + ((total/100) * percent)) / nPeople):.2f}")