import pygame

# pygame setup
pygame.init()
pygame.mixer.init()
width = 400
height = 640
screen = pygame.display.set_mode((width, height))
title = pygame.display.set_caption('Juego')
clock = pygame.time.Clock()
running = True
deltatime = 0
fps = 60

# game icon
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

# text font
font = pygame.font.Font("fonts/comicsans.ttf", 32)

# click sound
blop_sound = pygame.mixer.Sound("sounds/blop.mp3")

class Sprite():
    def __init__(self, image_src, x, y):
        self.image = pygame.image.load(image_src)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

egg = Sprite("images/egg.png", 0, 100)
close = Sprite("images/close.png", 326, 10)
reset = Sprite("images/reset.png", 246, 10)

# score 
score = 0

with open("data/score") as f:
    f_str = ""
    for l in f.readlines():
        f_str += l
    score = int(f_str.strip())

# score text
text = font.render("Score: "+str(score), False, 'black')

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        click = event.type == pygame.MOUSEBUTTONUP
        mouse_x, mouse_y = pygame.mouse.get_pos()
        # egg click
        if egg.rect.collidepoint(mouse_x, mouse_y):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if click:
                pygame.mixer.Sound.play(blop_sound)
                score += 1
                text = font.render("Score: "+str(score), False, 'black')
                print('yeah!')
        # close button
        elif close.rect.collidepoint(mouse_x, mouse_y):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if click:
                pygame.mixer.Sound.play(blop_sound)
                # save score
                with open("data/score", "w") as f:
                    f.write(str(score))
                running = False
        # reset button
        elif reset.rect.collidepoint(mouse_x, mouse_y):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if click:
                pygame.mixer.Sound.play(blop_sound)
                # reset score
                with open("data/score", "w") as f:
                    score = 0
                    text = font.render("Score: "+str(score), False, 'black')
                    f.write("0")
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # draw the egg
    screen.blit(egg.image, (egg.rect.x, egg.rect.y))
    
    # draw close button
    screen.blit(close.image, (close.rect.x, close.rect.y))

    # draw reset button
    screen.blit(reset.image, (reset.rect.x, reset.rect.y))
    
    # draw score text
    screen.blit(text, (20, 20))

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    deltatime = clock.tick(fps) / 1000

pygame.quit()
