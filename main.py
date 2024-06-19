# import turtle
#
# from turtle import *
#
# timmy = Turtle()
# print(timmy)
# # For method
# timmy.shape("turtle")
# turtle.color("DarkRed")
# timmy.forward(100)
#
# # For method
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import *

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"

print(table.align)
print(table)
