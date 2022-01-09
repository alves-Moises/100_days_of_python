#Life in Weeks

age = int(input("what is yout current age?"))

yearsLeft = 90 - age
daysleft  = 365 * (yearsLeft)
weeksleft = (int(365 / 7)) * yearsLeft
months = yearsLeft * 12

print(f'You have {daysleft}, {weeksleft} weeks and {months} months left')
