from turtle import *
def tri(size):
    for x in range(3):
        forward(size)
        left(180-(180/3))
        
for size in range (10, 150, 30):
    tri(size)

    
