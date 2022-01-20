#Write your code below this row 👇

for i in range(101):
    if(i%3 == 0):
        print('Fizz')
    if(i%5 == 0):
        print('Buzz')
    if(not(i%5 == 0) and not (i%3 == 0)):
        print(i)