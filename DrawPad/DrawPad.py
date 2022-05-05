

# ---- Imports ---- #
import pygame, sys, os, PIL, pygame_menu              # UPDATE PIL TO 9.1.0 AND PYGAME-MENU TO 4.2.7
from pygame.locals import *
from os import path
from os.path import exists
from PIL import Image

# ---- Variables ---- #
mposcoords = []
colour = (255, 0, 0)                                    # Default Colour
n = 0
drawnum = ("Exports/drawing{}.jpg").format(n)

# ---- Colours ---- #                                   # It's getting annoying manually entering values lol
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
grey = (69, 69, 69)

# ---- Initialization ---- #
pygame.init()                                           # Initializes pygame 
pygame.display.init()                                   # Initializes the display part of pygame
pygame.font.init()                                      # Initializes the font part of pygame

# ---- OS Pathfinding / Directory Creation ---- #
Path = os.getcwd()                                      # Finds the path the .py file is in
Expath = Path + "/Exports"                              # Adds an additional part to the path to be added
try:
    os.mkdir(Expath)                                    # Makes the new directory
except:
    pass

# ---- Main Window ---- #
pygame.display.set_caption('DrawPad')                   # Sets title of window
screen = pygame.display.set_mode()                      # Creates a window for the game to be in
dimensions = pygame.display.get_desktop_sizes()         # Grabs dimensions of desktop for window sizing

# ------ Resolution ------- #
try:
    dimensions = dimensions[0]                          # Accounts for dual monitors and single monitors
except:
    pass

resolution = dimensions
(windresx, windresy) = resolution                       # Unpacking the tuple for use as two variables

# ---- Drawing Subsurface ---- #
Drawingspace = (100, 50, windresx - 150, windresy - 100)# Rect
Drawscreen = screen.subsurface(Drawingspace)            # Creates a subsurface that can be 'screenshotted' later
Exportspace = pygame.Surface((windresx, windresy))
Exportspace.blit(Drawscreen, Drawingspace)

def quitfunc():
    raise quit()                                                               # This closes the program

# ---- Save Function ---- #
def keypress():
    global n                                                                   # Allows n to be changed outside and inside of the function 
                                                                               # (potentially unnesesary but I couldn't get it to work any other)
    # ---- Anti-Dupe ---- #
    exists = True
    while exists == True:                                                      # Checks for a duplicate file name before saving (This is to start on the right unused filename on startup)
        if os.path.exists(f'Exports/drawing{n}.jpg') == True:                   
            n += 1
            exists = True
   
        else:
            exists = False
            break

    # ---- Exporting ---- #                                                     # Debugging
    Exportspace.blit(Drawscreen, Drawingspace)                                  # "Saves" the screen to be exported
            
    if os.path.exists(f'Exports/drawing{n}.jpg') == True:                       # Checks if there is already a file with the same filename in the file
        n += 1

        pygame.image.save(Exportspace, f'Exports/drawing{n}.jpg')               # Saves the file to the folder path

        img = Image.open(f'Exports/drawing{n}.jpg')                             # Opens the image for cropping
        imgcrop = img.crop((100, 50, windresx - 50, windresy - 50))             # Crops the image
        imgcrop = imgcrop.save(f"Exports/drawing{n}.jpg")                       # Overwrites the image that was just saved                              

    elif os.path.exists(f'Exports/drawing{n}.jpg') == False:
        pygame.image.save(Exportspace, f'Exports/drawing{n}.jpg')  

        img = Image.open(f'Exports/drawing{n}.jpg')
        imgcrop = img.crop((100, 50, windresx - 50, windresy - 50))
        imgcrop = imgcrop.save(f"Exports/drawing{n}.jpg") 
    else:
        pass

# ---- Main Function ---- #
def mainfunc():

    screen.fill(grey)
    pygame.draw.rect(screen, white, Drawingspace)

    global colour                                                                       # Makes the colour variable useable in and outside the function

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        pygame.display.update()

        # ---- Colour Swatches ---- #
        pygame.draw.rect(screen, red, (25, 25, 50, 50))      # Red                      # Screen variable is the window
        pygame.draw.rect(screen, green, (25, 100, 50, 50))   # Green                    # First bracket tuple is RGB value
        pygame.draw.rect(screen, blue, (25, 175, 50, 50))    # Blue                     # Second bracket tuple is position
        pygame.draw.rect(screen, white, (25, 250, 50, 50))   # White                    # !! (distance from left, distance from top, x size, y size) !! (position for rect render)
        pygame.draw.rect(screen, black, (25, 325, 50, 50))   # Black
    
        # ---- Mouse Tracking ---- #
        mouse = pygame.mouse.get_pressed(num_buttons = 3)
        mpos = pygame.mouse.get_pos()

        mposcoords = mpos
        (mposx, mposy) = mposcoords                                                     # Unpacking another tuple to get mouse position in x and y coordinates

        # ---- Key Logic ---- #

        key = pygame.key.get_pressed()
    
        if key[pygame.K_s]:                                                             # Activates the save function
            keypress()

        # ---- Colour Selection ---- #
        if mposx >= 25 and mposx <= 75:                                                 # Colour Selection (For now will change later)
            if mposy >= 25 and mposy <= 75 and mouse == (False, False, True):           # Red
                colour = red

            if mposy >= 100 and mposy <= 150 and mouse == (False, False, True):         # Green
                colour = green

            if mposy >= 175 and mposy <= 225 and mouse == (False, False, True):         # Blue
                colour = blue

            if mposy >= 250 and mposy <= 300 and mouse == (False, False, True):         # White
                colour = white

            if mposy >= 325 and mposy <= 375 and mouse == (False, False, True):         # Black
                colour = black
        # ---- Drawing Logic ---- #
        try:
            if mouse == (True, False, False):
                if mposx  >= 100 and mposx <= windresx - 50 and mposy >= 50 and mposy <= windresy - 50: # Checks if mouse is in bounds of the canvas
                    pygame.draw.circle(screen, colour, mpos, 5)                                         # Draws a bunch of circles in place of a brush
                    pygame.display.update()
        except ValueError:
            pass
   
        # ---- Canvas Wipe ---- #
        if key[pygame.K_SPACE]:
            pygame.draw.rect(screen, white, Drawingspace)                                               # Fills drawing space with white

        if key[pygame.K_ESCAPE]:                                                                        # Exits back to main menu 
            mainmenufunc()

# ---- Menu ---- #
def mainmenufunc():
 
    customtheme = pygame_menu.themes.THEME_SOLARIZED.copy()                                             # Menu shenanigains (Still experimenting with)
    customtheme.title_background_color = grey
    customtheme.background_color = white
    customtheme.title_font_color = black
    customtheme.widget_font_color = black


    menu = pygame_menu.Menu('DrawPad', windresx, windresy, theme = customtheme)               # Loads the menu with the correct dimensions and theme

    menu.add.label("Controls for this program are on the GitHub Wiki.")
    menu.add.label("Have Fun!")
    menu.add.button('Draw!', mainfunc)
    menu.add.button("Quit", quitfunc)
    menu.mainloop(screen)
  
# ---- Calling functions ---- #

mainmenufunc()                                                                                             # Starts the program (Ironic it's at the end of the code)

pygame.quit()                                                                                              # When program is force closed

input('-Press Enter to Exit-')                                                                             # Habit


