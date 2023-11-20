import pygame
from fighter import Fighter

pygame.init()

# create game window
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Yeetfighter")

# cap the framerate
clock = pygame.time.Clock()
FPS = 90

# define colours
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

#define game variables
intro_count = 3
last_count_update = pygame.time.get_ticks()


# define fighter variables
STICKMAN_SIZE = 162  # character size withhin spritesheet
STICKMAN_SCALE = 4
STICKMAN_OFFSET = [72, 56] #find through testing
STICKMAN_DATA = [STICKMAN_SIZE, STICKMAN_SCALE, STICKMAN_OFFSET]
TEMPORARY_SIZE = 162
TEMPORARY_SCALE = 4
TEMPORARY_OFFSET = [72, 56]
TEMPORARY_DATA = [TEMPORARY_SIZE, TEMPORARY_SCALE, TEMPORARY_OFFSET]

# load a background image
bg_image = pygame.image.load("assets/images/background/template background.png").convert_alpha()

# load spritesheets
stickman_sheet = pygame.image.load("assets/images/character tom/Spritesheet.png").convert_alpha()
temporary_sheet = pygame.image.load("assets/images/character tom/Spritesheet.png").convert_alpha()

# define number of frames per animation
STICKMAN_ANIMATION_STEPS = [10, 8, 1, 7, 7, 3, 7]
TEMPORARY_ANIMATION_STEPS = [10, 8, 1, 7, 7, 3, 7]


# function to display background image
def draw_bg():
    # if background image needs to be stretched
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))


# creating health bars
def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE,
                     (x - 4, y - 4, 408, 38))  # the following three lines are only for aesthetic UI purposes
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))


# create fighters instances
fighter_1 = Fighter(1, 200, SCREEN_HEIGHT-400, False, STICKMAN_DATA, stickman_sheet, STICKMAN_ANIMATION_STEPS)
fighter_2 = Fighter(2, SCREEN_WIDTH-280, SCREEN_HEIGHT-400, True,  TEMPORARY_DATA, temporary_sheet,TEMPORARY_ANIMATION_STEPS)  # the temporary ones are temporary place holders for it to work

#animation hit issue
delay = 0

# create game loop (never load sprites/images withhin gameloop if background)
running = True
while running:

    clock.tick(FPS)

    # draw background
    draw_bg()

    delay += 1
    if delay >=4:
        delay = delay -4

    # draw healthbars/show player stats
    draw_health_bar(fighter_1.health, 20, 20)
    draw_health_bar(fighter_2.health, SCREEN_WIDTH - 420, 20)

    #update beginning countdown
    if intro_count <= 0:

    # move fighters
        fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2)
        fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1)
    else:
        #update countdown timer
        if (pygame.time.get_ticks() - last_count_update) >= 1000:
            intro_count -=1
            last_count_update = pygame.time.get_ticks()
            print(intro_count)

    #update fighter animation
    fighter_1.update(screen,fighter_2)
    fighter_2.update(screen, fighter_1)

    # draw the character instances
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # display update
    pygame.display.update()

# exit pygame
pygame.quit()
