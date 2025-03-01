import pygame
import sys

# Initialize screen width and height
SW, SH = 1000, 1000

# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((SW, SH))
pygame.display.set_caption("checkered")

# Set up the clock for controlling the frame rate
tps = pygame.time.Clock()

# Set up the font for text display
font = pygame.font.SysFont("arial", 50)

# Get the number of squares in horizontal and vertical directions from the user
square_amount_X = int(input("what is the amount of squares in horizontal? : "))
square_amount_Y = int(input("what is the amount of squares in vertical? : "))

def CREATE_CHESSBOARD():
    # Define colors
    white = (255, 255, 255)
    black = (0, 0, 0)
    
    # Calculate the width and height of each rectangle
    rect_width = SW / square_amount_X
    rect_height = SH / square_amount_Y

    # Draw the chessboard
    for i in range(square_amount_X):
        for j in range(square_amount_Y):
            if (i + j) % 2 == 0:
                color = white
            else:
                color = black
            pygame.draw.rect(screen, color, (i * rect_width, j * rect_height, rect_width, rect_height))

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Draw the chessboard
    CREATE_CHESSBOARD()
    
    # Update the display
    pygame.display.update()
    
    # Control the frame rate
    tps.tick(1)