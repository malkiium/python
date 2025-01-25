import pygame
import sys

SW, SH = 900, 900
pygame.init()
screen = pygame.display.set_mode((SW,SH))
pygame.display.set_caption("checkered")
tps = pygame.time.Clock()
font = pygame.font.SysFont("arial", 50)
square_amount_X = int(input("what is the amount of squares in horizontal? :"))
square_amount_Y = int(input("what is the amount of squares in vertical? :"))


def CREATE_CHESSBOARD():
    white = (255,255,255)
    black = (0,0,0)
    rect_width = SW/square_amount_X
    rect_height = SH/square_amount_Y

    for i in range(square_amount_X):
        for j in range(square_amount_Y):
            if (i+j)%2 == 0:
                color = white
            else:
                color = black
            pygame.draw.rect(screen, color, (i * rect_width, j * rect_height, rect_width, rect_height))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    CREATE_CHESSBOARD()  # Draw the chessboard
    pygame.display.update()  # update everything
    tps.tick(10)  # fps