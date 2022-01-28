from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)

bid = dict()
while True:
    name = input("your name:")
    bid_amount = float(input("Your bid: "))
    bid[name] = bid_amount

    more_one = input("Do you wanna add one more people to bid? [y] [n]").lower()
    if more_one == 'n':
        break

    clear()
best = 0

for name in bid:
    if bid[name] > best:
        best = bid[name]
        best_name = name

clear()
print("name:", best_name)
print(f"Value: {best}")
