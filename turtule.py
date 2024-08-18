import random
from turtle import Turtle, Screen


shapes = ["turtle", "square", "square",
          "triangle", "circle", "classic", "arrow"]


colors = ["red", "orange", "yellow", "green",
          "black", "CadetBlue", "midnightBlue"]

sizes = [2, 4, 6, 8, 10, 12]

ahmed = Turtle('turtle')
window = Screen()

for _ in range(4):
    ahmed.shape(random.choice(shapes))
    ahmed.color(random.choice(colors))
    ahmed.pensize(random.choice(sizes))
    ahmed.forward(100)
    ahmed.left(90)


window.exitonclick()
