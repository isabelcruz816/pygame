import pygame
pygame.init()

SCREENWIDTH = 500

win = pygame.display.set_mode((SCREENWIDTH,SCREENWIDTH))
pygame.display.set_caption("First Game")

x = 50
y = 50
width = 40
height = 60
vel = 5

running = True

while running:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel

    if keys[pygame.K_RIGHT] and x < SCREENWIDTH - width - vel:
        x += vel

    if keys[pygame.K_UP] and y < vel:
        y -= vel

    if keys[pygame.K_DOWN] and y > SCREENWIDTH - height - vel:
        y += vel
    
    win.fill((0,0,0))
    pygame.draw.rect(win, (255,0,0), (x, y, width, height))   
    pygame.display.update() 
    
pygame.quit()