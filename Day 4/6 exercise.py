# 🚨 Don't change the code below 👇
from turtle import pos


row1 = ["[]","[]","[]"]
row2 = ["[]","[]","[]"]
row3 = ["[]","[]","[]"]
maps = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
maps[int(str(position)[1])] [int(str(position)[0])] = 'x'
  


#Write your code above this row 

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")