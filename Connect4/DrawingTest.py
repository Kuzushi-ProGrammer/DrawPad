# Resizable window
# Find a way to update it faster (or) find a way make smooth lines
# RGB Colour picker (Wheel or manual entry)
# Colour picker (Off Canvas)
# Transparency (o-o)

# Menu
    # Store image when in menu so it doesn't get wiped
    # Export Feature
    # Change Background Colour
    # Controls

# ---- Imports ---- #
import pygame, sys, os, PIL
from pygame.locals import *
from os import path
from os.path import exists
from PIL import Image

# ---- Variables ---- #
mposcoords = []
colour = (255, 0, 0)                                    # Default Colour
n = 0
drawnum = ('Exports/drawing{}.jpg').format(n)

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
Expath = Path + "/Exports"                             # Adds an additional part to the path to be added
try:
    os.mkdir(Expath)                                       # Makes the new directory
except:
    pass
print(Expath)
print(Path)

# ---- Main Window ---- #
pygame.display.set_caption('Drawing Test Program')      # Sets title of window
screen = pygame.display.set_mode()                      # Creates a window for the game to be in
dimensions = pygame.display.get_desktop_sizes()         # Grabs dimensions of desktop for window sizing

# ------ Resolution ------- #
try:
    dimensions = dimensions[0]                          # Accounts for dual monitors and single monitors
except:
    pass

resolution = dimensions
(windresx, windresy) = resolution

# ---- Drawing Subsurface ---- #
Drawingspace = (100, 50, windresx - 150, windresy - 100)# Rect
Drawscreen = screen.subsurface(Drawingspace)            # Creates a subsurface that can be 'screenshotted' later
Exportspace = pygame.Surface((windresx, windresy))
Exportspace.blit(Drawscreen, Drawingspace)

# ---- Initial Interface ---- #
screen.fill(grey)
pygame.draw.rect(screen, white, Drawingspace)

#Don't actually need this for now
#Leftside = (0, 0, 100, windresx - 50)                   # Position from left, position from top, width, height
#Topside = (0, 0, windresx, 50)                          # Variables for drawing the bars
#Rightside = (windresx - 50, 0, 50, windresy)
#Bottomside = (0, windresy - 50, windresx, 50)

# ---- Anti-Dupe ---- #
exists = True
while exists == True:
    if os.path.exists(f'Exports/drawing{n}.jpg') == True:                       # Currently overwrites files of same name (Not intentional)
            n += 1
            exists = True
   
    else:
        exists = False
        continue

# ------------------------------------------------------------------------------- # MAIN LOOP
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

    #pygame.draw.rect (screen, grey, Leftside)           # Left sidebar             
    #pygame.draw.rect (screen, grey, Topside)            # Top sidebar
    #pygame.draw.rect (screen, grey, Rightside)          # Right sidebar
    #pygame.draw.rect (screen, grey, Bottomside)         # Bottom sidebar
    
# ---- Colour Swatches ---- #
    pygame.draw.rect(screen, red, (25, 25, 50, 50))      # Red                      # Screen variable is the window
    pygame.draw.rect(screen, green, (25, 100, 50, 50))   # Green                    # First bracket tuple is RGB value
    pygame.draw.rect(screen, blue, (25, 175, 50, 50))    # Blue                     # Second bracket tuple is position
    pygame.draw.rect(screen, white, (25, 250, 50, 50))   # White                    # !! (distance from left, distance from top, x size, y size) !! (position for rect render)
    pygame.draw.rect(screen, black, (25, 325, 50, 50))   # Black
    
# ---- Mouse Tracking ---- #
    mouse = pygame.mouse.get_pressed(num_buttons = 3)
    mpos = pygame.mouse.get_pos()
    key = pygame.key.get_pressed()

    mposcoords = mpos
    (mposx, mposy) = mposcoords

# ---- Colour Selection ---- #
    if mposx >= 25 and mposx <= 75:
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
            if mposx  >= 100 and mposx <= windresx - 50 and mposy >= 50 and mposy <= windresy - 50:
                pygame.draw.circle(screen, colour, mpos, 5)
                pygame.display.update()
    except ValueError:
        pass
   
# ---- Canvas Wipe ---- #
    if key[pygame.K_SPACE]:
        pygame.draw.rect(screen, white, Drawingspace)

# ---- Exporting ---- #
    if key[pygame.K_s]:
        pressed = True
        while pressed == True:
            print(os.path.exists(f'Exports/drawing{n}.jpg'))
            Exportspace.blit(Drawscreen, Drawingspace)                                  # Also saves with left and top black bars (has something to do with the surface)
            
            if os.path.exists(f'Exports/drawing{n}.jpg') == True:                       # Currently overwrites files of same name (Not intentional)
                n += 1

                pygame.image.save(Exportspace, f'Exports/drawing{n}.jpg')  

                img = Image.open(f'Exports/drawing{n}.jpg')
                imgcrop = img.crop((100, 50, windresx - 50, windresy - 50))
                imgcrop = imgcrop.save(drawnum)

                print('Saved! (True)')
                pressed = False

            else:
                pygame.image.save(Exportspace, f'Exports/drawing{n}.jpg')  

                img = Image.open(f'Exports/drawing{n}.jpg')
                imgcrop = img.crop((100, 50, windresx - 50, windresy - 50))
                imgcrop = imgcrop.save(drawnum)

                print('Saved! (False)')
                pressed = False

pygame.quit()



'''                                                                 # Sample code for reference
# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Flip the display
    pygame.display.flip()                                           # Updates the image on screen

pygame.quit()

'''

input('-Press Enter to Exit-')


