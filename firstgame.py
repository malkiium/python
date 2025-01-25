import pygame
import sys
import random


SW, SH = 1000, 900
BLOCK_SIZE = 50
dark_green = "#66CC00"

pygame.init() #init = initialise. it initialises the screen
screen = pygame.display.set_mode((SW, SH))
FONT = pygame.font.SysFont("arial", 100)
pygame.display.set_caption("snake")
tps = pygame.time.Clock()

def drawGrid():
    for x in range(0, SW, BLOCK_SIZE):
        for y in range(0, SH, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, "#3c3c3b", rect, 1)

class Snake:
    def __init__(self):
        self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
        self.xdir = 1
        self.ydir = 0
        self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
        self.body = [pygame.Rect(self.x-BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
        self.dead = False
    def update(self):
        global apple
        for square in self.body:
            if self.head.x == square.x and self.head.y == square.y:
                self.dead = True
            if self.head.x not in range(0, SW) or self.head.y not in range(0, SH):
                self.dead = True

        if self.dead:
            self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
            self.xdir = 1
            self.ydir = 0
            self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
            self.body = [pygame.Rect(self.x - BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
            self.dead = False
            apple = Apple()

        self.body.append(self.head)
        for i in range(len(self.body)-1):
            self.body[i].x, self.body[i].y = self.body[i+1].x, self.body[i+1].y
        self.head.x += self.xdir * BLOCK_SIZE
        self.head.y += self.ydir * BLOCK_SIZE
        self.body.remove(self.head)
snake = Snake()

class Apple:
    def __init__(self):
        self.x = int(random.randint(0, SW)/BLOCK_SIZE) * BLOCK_SIZE
        self.y = int(random.randint(0, SH)/BLOCK_SIZE) * BLOCK_SIZE
        self.rect = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
    def update(self):
        pygame.draw.rect(screen, "red", self.rect)
apple = Apple()

score = FONT.render("1", True, "white")
score_rect = score.get_rect(center=(SW/2, SH/20))

while True:
    #draw all the elements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #un-initialise the screen
            sys.exit() #stops the code : like a break(), but less ugly. it closes the code
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                snake.ydir = 1
                snake.xdir = 0
            if event.key == pygame.K_UP:
                snake.ydir = -1
                snake.xdir = 0
            if event.key == pygame.K_RIGHT:
                snake.ydir = 0
                snake.xdir = 1
            if event.key == pygame.K_LEFT:
                snake.ydir = 0
                snake.xdir = -1

    snake.update()
    screen.fill("black")
    drawGrid()
    apple.update()
    score = FONT.render(f"{len(snake.body)-1}", True, "white")

    pygame.draw.rect(screen, "green", snake.head) #draw head
    for square in snake.body: #draw body
        pygame.draw.rect(screen, dark_green, square)

    screen.blit(score, score_rect)

    if snake.head.x == apple.x and snake.head.y == apple.y: #eating apple
        snake.body.append(pygame.Rect(square.x, square.y, BLOCK_SIZE, BLOCK_SIZE)) #add length to body
        apple = Apple() #respawn apple


    pygame.display.update() #update everything
    tps.tick(7) #fps