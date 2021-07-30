import pygame
import random

# Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('wepik-2021628-1353.png')

# Title and Icon
pygame.display.set_caption("SPACE INVADERS")
icon = pygame.image.load('space-invaders.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
x_delta = 0
y_delta = 0

# Enemy
enemyImg = pygame.image.load('alien-pixelated-shape-of-a-digital-game.png')
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_delta = 2.5
enemyY_delta = 40

# Bullet

# Ready - You Can't See the Bullet on the Screen
# Fire - The Bullet is Currently Moving

bulletImg = pygame.image.load('bullet1.png')
bulletX = 0
bulletY = 0
bulletX_delta = 0
bulletY_delta = 5
bullet_state = "ready"




down_x_count = 0
down_y_count = 0

KEYS = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_UP]

def player(x,y):
    screen.blit(playerImg,(x, y))

def enemy(x,y):
    screen.blit(enemyImg,(x, y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

# Game Loop
running = True
while running:

    # RGB - Red, Green, Blue
    screen.fill((120, 180, 240))

    # Background Image
    screen.blit(background,(0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                down_x_count += 5
                x_delta = -5
                print('left key is pressed')
            if event.key == pygame.K_RIGHT:
                down_x_count += 5
                x_delta = 5
                print('right key is pressed')
            if event.key == pygame.K_UP:
                down_y_count += 5
                y_delta = -5
                print('up key is pressed')
            if event.key == pygame.K_DOWN:
                down_y_count += 5
                y_delta = 5
                print('down key is pressed')
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    # Get the Current X Coordinate of the Spaceship
                    bulletX = playerX
                    bulletY = playerY
                    fire_bullet(bulletX, bulletY)


        if event.type == pygame.KEYUP:
            print('key is released')
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                down_x_count -= 5
                if down_x_count == 0:
                    x_delta = 0
            if event.key in [pygame.K_UP, pygame.K_DOWN]:
                down_y_count -= 5
                if down_y_count == 0:
                    y_delta = 0



    # Checking for Boundaries of Player
    playerX += x_delta
    playerY += y_delta
    if playerX < 0:
        playerX = 0
    if playerX > (800 - 64):
        playerX = (800 - 64)
    if playerY < 0:
        playerY = 0
    if playerY > (600 - 64):
        playerY = (600 - 64)

    # Enemy Movement
    enemyX += enemyX_delta

    if enemyX <= 0:
        enemyX_delta = 2.5
        enemyY += enemyY_delta
    elif enemyX >= 736:
        enemyX_delta = -2.5
        enemyY += enemyY_delta

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_delta



    player(playerX,playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()