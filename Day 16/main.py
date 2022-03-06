# import another_module
# print(another_module.another_variable)

# from turtle import Turtle, Screen, exitonclick

# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color(("#000"), ("#fde"))


# my_screen = Screen()
# timmy.forward(100)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column('Pokemon Name',["Pikachu", "Squirtle", "Charmander"])
table.add_column('Type', ["Eletric", "Water", "Fire"])

table.align = 'l'
print(table)


