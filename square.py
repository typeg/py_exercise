from turtle import *

reset()
def square(size):
        for x in range(4):
                forward(size)
                right(90)

for size in range(10, 100, 30):
    square(size)
    
