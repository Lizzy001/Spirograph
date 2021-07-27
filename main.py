import turtle as t
import random

lizzy = t.Turtle()
t.colormode(255)


#
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


lizzy.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        lizzy.color(random_color())
        lizzy.circle(100)
        lizzy.setheading(lizzy.heading() + size_of_gap)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
