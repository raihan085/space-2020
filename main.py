import pygame
import random

# Initialize the pygame
pygame.init()

# Create the screen
width = 600
height = 600
screen = pygame.display.set_mode((width, height))


# Add background
background = pygame.image.load("background.png")

# Add Title and Icon
titleLink = "Space 2020"
iconLink = "ufo.png"
pygame.display.set_caption(titleLink)
icon = pygame.image.load(iconLink)
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load("player.png")
playerX = 270
playerY = 450
player_change = 0
playerY_change = 0


def player(playerX,playerY):
    screen.blit(playerImg,(playerX,playerY))


# Enemy
enemyImg = pygame.image.load("enemy.png")
enemX = random.randint(64,600-64)
enemY = random.randint(50,150)
enemyX_change = 3
enemyY_change = 20


def enemy(enemX,enemY):
    screen.blit(enemyImg,(enemX,enemY))


# Bullet
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 380
bulletX_change = 0
bulletY_change = 5

# Ready - you can't see the bullet on the screen
# Fire - The bullet is currently moving

bullet_state = "ready"


def bullet_fire(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x+16,y+10))


# Game Loop
running = True

while running:

    # Add Background Color : RGB = Red,Green,Blue
    screen.fill((0,0,0))
    screen.blit(background,(0,0))

    # when we click x button then the program exicuted
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_change = -1
            if event.key == pygame.K_RIGHT:
                player_change = 1
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    # Get the current x co-ordinate of the spaceship
                    bulletX = playerX
                    bullet_fire(bulletX,bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_change = 0


    # Bullet moving
    if bulletY <= 0:
        bulletY = 380
        bullet_state = "ready"

    if bullet_state is "fire":
        bullet_fire(bulletX,bulletY)
        bulletY -= bulletY_change

    # Add Player
    playerX += player_change


    # boundary condition of player
    if playerX <= 0:
        playerX = 0
    elif playerX >= 600-64:
        playerX = 600-64

    player(playerX,playerY)

    # add enemy
    enemX += enemyX_change

    # boundary condition of enemy
    if enemX <= 0:
        enemyX_change = 3
        enemY += enemyY_change
    elif enemX >= 600-64:
        enemyX_change = -3
        enemY += enemyY_change

    enemy(enemX, enemY)
    # update display
    pygame.display.update()