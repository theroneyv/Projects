import pygame
import random

# pygame setup
pygame.init()
width = 640
height = 480
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
deltatime = 0
fps = 60

player = pygame.Rect(width / 2 - 16, height - 32, 32, 32)
player_speed = 300

food = pygame.Rect(random.randint(0, width - 16), 0, 32, 32)
food_speed = 150

score = 0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # player movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player.x -= player_speed * deltatime
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player.x += player_speed * deltatime

    # draw player
    pygame.draw.rect(screen, "white", player)

    # food movement
    if food.y < height:
        food.y += food_speed * deltatime
    else:
        food.y = 0

    # score
    if food.colliderect(player):
        food.y = 0
        food.x = random.randint(0, width - 16)
        score += 1
        food_speed += 10
        player_speed += 10
        print('Score:', score) 

    # draw food
    pygame.draw.rect(screen, "red", food) 

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    deltatime = clock.tick(fps) / 1000

pygame.quit()