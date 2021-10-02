import turtle
# turtle is a pre-installed Python library that enables users to create pictures and shapes by providing them with a virtual canvas
import random

count=0

def circle():
    global count
    t= turtle.Turtle()
    turtle.bgcolor("black")
    colors=["red","blue","pink","white","cyan","green","violet","yellow"]
    # get a random color 
    random_color = random.choice(colors)
    t.color(random_color)
    print(random_color)
    t.forward(1) # start from center
    t.speed(0.05) # increasing htis will slow the speed
    while True:
        t.circle(70)
        t.right(3)
        t.forward(3)
        count+=1 # this count is the time taken for 1 spin with speed 0.05, if the speed is altered then count should be changed accordingly 
        if count == 120:
            count=0 
            t.clear() # this will clear the screen and call the circle function again with new random color circle
            circle()

if __name__ == "__main__":
    circle()