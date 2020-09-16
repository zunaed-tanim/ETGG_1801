# Could ID-Section  : ETGG1801.90
# Name              : Md Zunaed Tanim
# Lab               : 2 / Expressions
# Date Created      : 16 September, 2020
# Git Repository    : https://github.com/zunaed-tanim/ETGG_1801/blob/Lab-02/main.py

# import Pillow library
import PIL.Image

# ------------------ STEP 03 ------------------

# Drawing a coffee cup ASCII art with multiple print statements
print("\n      \'   \'   \'")
print("\t \' \t \' \t \"")
print("   \'   \"   \"   \"")
print("\t \" \t \" \t \" \t \"")
print("_______________________")
print("\\_____________________/")
print(" \\                   /===/")
print("  \\                 /\t/")
print("   |               /   /")
print("   /              /   /")
print("  /              /===/")
print("  \\_____________/")


# ------------------ STEP 04 ------------------

# Drawing a coffee cup ASCII art with a single print statement
print('''
\n      \'   \'   \'
\t \' \t \' \t \"
   \'   \"   \"   \"
\t \" \t \" \t \" \t \"
_______________________
\\_____________________/
 \\                   /===/
  \\                 /\t/
   |               /   /
   /              /   /
  /              /===/
  \\_____________/

''')


# ------------------ STEP 05 ------------------


# Ask user to enter ASCII health bar art characters for single health unit
healthUnit = input("Enter your ASCII Health Bar Art Characters: \n")
# Ask user to enter their preferred health count for health bar and covert it to integer
maxHealthCount = int(input("Please enter your preference for the Health Bar length: "))
# Calculate maximum health for ASCII art
maxHealth = healthUnit * maxHealthCount
# Print health bar with maximum health
print("Health Bar with maximum health:\n" + maxHealth)
# Calculate the health bar length
barLength = len(maxHealth)
# Ask the user how much health player has lost and convert the value to integer
lostHealth = int(input("Please enter player's lost health count: "))
# Get current health count of the player
currentHealthCount = maxHealthCount - lostHealth
# Calculate current health for ASCII art
currentHealth = healthUnit * currentHealthCount


def health_check():
    if lostHealth < maxHealthCount and currentHealthCount > 0:
        print("Your player is still in the game [^_^] ! Player's current health is: " + str(currentHealthCount))
        print(currentHealth)
    if lostHealth == maxHealthCount:
        print("Ops! You've lost your player [+_+] ... " + "Current Health:", currentHealthCount)
    if currentHealthCount < 0:
        print("You entered invalid value for player's lost health. " + "Try again!")


# Call the function
health_check()

# ------------------ STEP 06, 07, 08 ------------------

# Halt the program until the user presses enter
input("Press enter to continue...")

# ***-- The program below prints ASCII image from an image file --*** #

# Define list of ASCII characters
ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]


# resize image according to a new width
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image


# convert each pixel to grayscale
def converted_grayscale(image):
    grayscale_image = image.convert("L")
    return grayscale_image


# convert pixels to a string of ascii characters
def ascii_from_pixels(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return characters


def main_ascii(new_width=100):
    # approach to open image from user-input
    path = input("Enter a valid pathname to an image: ")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, " -is an invalid pathname to an image. Please try again")
        return

    # convert image to ascii
    new_image_data = ascii_from_pixels(converted_grayscale(resize_image(image)))

    # format
    pixel_count = len(new_image_data)
    ascii_image = "\n".join([new_image_data[index:(index + new_width)] for index in range(0, pixel_count, new_width)])

    # print result
    print(ascii_image)

    # save result to "ascii_image.txt"
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)


# run program
main_ascii()



"""
* Note: When I was researching ASCII art, I came across the option to convert image to ASCII art, wanted to try it.
        I found different approaches, but I liked the cleanliness and ease of understanding of the above approach.
        I slightly modified the code but followed along mostly from the original sources (See below) 
        since I liked it as it is. Didn't feel the need to modify too much. 
        Sources: https://github.com/kiteco/python-youtube-code/commit/663dc86d8bcab7d3f1d0e5388771ea7889994fc5,
        https://medium.com/javascript-dots/python-ascii-art-generator-60ba9eb559d7 
"""


