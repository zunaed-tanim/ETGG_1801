"""
# Course ID-Section : ETGG1801.90
# Name              : Md Zunaed Tanim
# Lab               : 2 / Expressions
# Date Created      : 16 September, 2020
# Git Repository    : https://github.com/zunaed-tanim/ETGG_1801.git
"""

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

# Halt the program until the user presses enter
input("Press enter to continue...")


