"""
from turtle import forward, left, exitonclick
for x in range(3):
    for i in range(4):
        forward(50)
        left(90)
    left(20)

exitonclick()
"""
"""
from turtle import forward, left, right, exitonclick
for i in range(5):
    forward(100)
    left(90)
    forward(100)
    right(90)
exitonclick()
"""
"""
from turtle import forward, left, right, exitonclick
for j in range(6):
    for i in range(6):
        left(60)
        forward(100)
    right(60)
    forward(100)
exitonclick()
"""
"""
from turtle import forward, left, exitonclick, penup, pendown
for i in range(360):
    forward(i // 10 + 1)
    left(10)
    penup()
    forward(i // 10 + 1)
    left(10)
    pendown()
exitonclick()
"""