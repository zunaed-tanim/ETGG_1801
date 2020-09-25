# ------------------ STEP 02 ------------------

# Course ID-Section : ETGG1801.90
# Name              : Md Zunaed Tanim
# Lab               : 3 / Modules
# Date Created      : 25 September, 2020
# Git Repository    : https://github.com/zunaed-tanim/ETGG_1801/blob/Lab-02/MdZunaed_TanimLab03.py

# ------------------ STEP 03 ------------------

import pygame
import time
import random
from pygame.locals import *

# Initializing pygame display features
pygame.display.init()

# Set up the drawing window
WIDTH = 1000
HEIGHT = 1000
window = pygame.display.set_mode((WIDTH, HEIGHT))
win_center = (WIDTH - (WIDTH//2), HEIGHT - (HEIGHT//2))

# Name the window
pygame.display.set_caption("Lab 03 by Tanim")

# ------------------ BONUS + STEP 04, 05, 06, 07 ------------------

# Variable to keep the main loop running
running = True

# Main Loop
while running:
    # Update the display by flipping buffers
    pygame.display.update()
    # Check every event in the loop
    for event in pygame.event.get():
        # Check if user pressed a key
        if event.type == KEYDOWN:
            # Check if the key pressed if escape key,
            if event.key == K_ESCAPE:
                # Halt the program for 10 seconds before closing
                time.sleep(10)
                # if so, stop the loop
                running = False
        # Check if window close button was clicked instead
        elif event.type == QUIT:
            # Halt the program for 10 seconds before closing
            time.sleep(10)
            # if so, stop the loop
            running = False

    # Drawing a small pixel robot on the surface
    window.fill((0, 0, 0))
    # Circle / Robot Eye
    pygame.draw.circle(window, (0, 0, 255), win_center, 30)
    # Ellipses / Robot Eye
    pygame.draw.ellipse(window, (0, 255, 255), (450, 400, 80, 80), 20)
    pygame.draw.ellipse(window, (255, 0, 0), (470, 420, 40, 40), 10)
    # Rectangles
    # Robot Head
    pygame.draw.rect(window, (255, 255, 255), (400, 350, 200, 200), 40)     # Head Main frame (White)
    pygame.draw.rect(window, (0, 0, 0), (400, 350, 200, 200), 10)           # Head Main frame Inner (Black)
    # Robot Body
    pygame.draw.rect(window, (0, 250, 190), (400, 600, 200, 160))           # Body Main frame
    pygame.draw.rect(window, (200, 0, 80), (400, 580, 100, 10))             # Body-Head Connector
    pygame.draw.rect(window, (0, 0, 0), (500, 600, 20, 100))                # Vertical Long black 1
    pygame.draw.rect(window, (0, 0, 0), (540, 600, 20, 100))                # Vertical Long black 2
    pygame.draw.rect(window, (0, 0, 0), (560, 620, 20, 20))                 # Small black square left upper
    pygame.draw.rect(window, (0, 0, 0), (580, 660, 20, 20))                 # Small black square right lower
    pygame.draw.rect(window, (0, 0, 0), (560, 640, 60, 40), 10)
    # Robot float/boost
    pygame.draw.rect(window, (180, 255, 0), (420, 760, 160, 20))            # Larger green bar
    pygame.draw.rect(window, (100, 245, 0), (430, 780, 140, 10))            # Smaller green bar

    # Drawing random circle (representing colorful snow) around the Robot
    # Declare variables that generate random values
    rand_position = random.random() * 900
    rand_pos = int(rand_position)                                           # Random position
    rand_siz = random.randint(10, 30)                                       # Random size
    rand_col = random.randrange(0, 255, 5)                                  # Random color
    # Snows in random colors, sizes, positions
    pygame.draw.circle(window, (0, 0, rand_col), (rand_pos, rand_pos), rand_siz)
    pygame.draw.circle(window, (0, rand_col, 0), (rand_pos, rand_pos), rand_siz)
    pygame.draw.circle(window, (rand_col, 0, 0), (rand_pos, rand_pos), rand_siz)
    pygame.draw.circle(window, (rand_col, 0, rand_col), (rand_pos, rand_pos), rand_siz)
    pygame.draw.circle(window, (rand_col, rand_col, rand_col), (rand_pos, rand_pos), rand_siz)
    pygame.draw.circle(window, (rand_col, rand_col, rand_col), (rand_pos, rand_pos), 20)

# Exit pygame
pygame.quit()
