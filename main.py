# pygame.init()  ->   Game Logic   ->   pygame.quit()
# display_surface (has width and height) -> the canvas to draw on
# game loop -> game logic and canvas update

import pygame, sys

def draw_floor():
    screen.blit(floor_surface, (floor_x, 700))
    screen.blit(floor_surface, (floor_x + 500, 700))

# Initialize Pygame
pygame.init()

# This is the display surface
# width = 576, height = 1024
screen = pygame.display.set_mode((500, 750)) 

# We can use clock.tick(frame_rate) later
clock = pygame.time.Clock()

# Game Variables
gravity = 0.25
bird_movement = 0

# convert -> it converts the image into a type of file while is easier for pygame
bg_surface = pygame.image.load('assets/background-day.png').convert()

# This scales up the background image by a factor of 2
bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load('assets/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x = 0

# load the bird
bird_surface = pygame.image.load('assets/bluebird-midflap.png').convert()
bird_surface = pygame.transform.scale2x(bird_surface)
# This takes the bird_surface and puts a rectangle around it. 
# A rectangle can help us for collision detection.
# center = (x, y) are the coordinated for the center of the rect
# We cna also set the coordinated for top_left, bottom_right etc.
bird_rect = bird_surface.get_rect(center = (100, 375))

# Game Loop
while True:
    # Here pygame looks for all the events that is happening right now
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            # even after pygame.quit() the pygame.display.update() command
            # is running, so sys.exit() will exit completely
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                bird_movement = 0
                bird_movement -= 5

    # blit puts one surface on another surface
    screen.blit(bg_surface, (0, 0))

    bird_movement += gravity
    print("bird_movement = %.2f" %bird_movement)
    # centery is the y coordinate of the rect
    bird_rect.centery += bird_movement
    screen.blit(bird_surface, bird_rect)
    draw_floor()
    floor_x -= 2
    if floor_x <= -500:
        floor_x = 0

    # This will take everything above it and display it in the screen
    pygame.display.update()
    clock.tick(50)