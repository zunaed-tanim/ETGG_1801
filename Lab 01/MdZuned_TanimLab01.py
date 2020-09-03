# ------------------------------ STEP 02 --------------------------------

# Course ID.Section      : ETGG1801.90
# First Name & Last Name : Md Zunaed, Tanim
# Lab Number & Name      : Lab 01 - Hello World
# Date created           : 02 September, 2020
# Git Repository         : https://github.com/zunaed-tanim/ETGG_1801

# *********************************************************
# importing math library to calculate hypotenuse in step 04
import math
# importing turtle module for BONUS
import turtle
# *********************************************************

# ------------------------------ STEP 03 ---------------------------------

# Creating variables
"""
* firstName - string
* lastName - string
* opposite - float
* adjacent - integer
"""
firstName = "Md Zunaed"
lastName = "Tanim"
opposite = float(input("Please enter a number value for opposite: "))
adjacent = int(input("Please enter a number value for adjacent: "))


# ------------------------------ STEP 04 ---------------------------------

# Printing firstName and lastName to the screen
print("Lab01 created by:", firstName, lastName)

# Printing firstName and lastName to the screen, using the end parameter, with two print statements
print(firstName, end=" ")
print(lastName)

# Calculating the hypotenuse from opposite & adjacent
hypotenuse = math.hypot(opposite, adjacent)
print("The hypotenuse length is " + str(hypotenuse) + ", if the other sides are " + str(adjacent) + " and " + str(opposite))

input("Press enter to continue...")

# ------------------------------ B O N U S ---------------------------------

print("I see you've made it. Alright, now let's see if we can draw a triangle with the number values you entered")

screen = turtle.Screen()                    # creating a new screen
screen.setup(1000, 1000)                    # set up the window size

fastTurtle = turtle.Turtle()                # creating an future speedy/fast turtle
screen.bgcolor("black")                     # set the background color to black
fastTurtle.color("aquamarine")              # Set turtle color
fastTurtle.shape("turtle")                  # Finally Mr FastTurtle gets his turtle shape


def triangle():
    fastTurtle.backward(adjacent)
    fastTurtle.left(90)
    fastTurtle.forward(opposite)
    fastTurtle.right(135)
    fastTurtle.forward(hypotenuse)


triangle()


print("Let's see if your entered values drew a perfect triangle or not...")
if adjacent == opposite:
    print("Well done! It's a perfect triangle! Here, enjoy there almond triangle cookies!")
    screen.bgpic("AlmondTriangleCookies.png")
else:
    print("Nope, that's not a perfect triangle. No cookies for you this time... Why not try again?")


turtle.done()
