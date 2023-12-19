import pygame
from fighter import Fighter
from menu import showWelcomeAnimation

# letting user pick character
USER_1 = 3  # int(input("Player one choose Character: 0 = Stickman, 1= Pizza Guy, 2 = Vincent\n"))
USER_2 = 3  # int(input("Player two choose Character: 0 = Stickman, 1= Pizza Guy, 2 = Vincent\n"))
#map = 3

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

# define game variables
intro_count = 0
last_count_update = pygame.time.get_ticks()

# define fighter variables
STICKMAN_SIZE = 162  # character size withhin spritesheet
STICKMAN_SCALE = 4
STICKMAN_OFFSET = [72, 56]  # find through testing
STICKMAN_DATA = [STICKMAN_SIZE, STICKMAN_SCALE, STICKMAN_OFFSET, 0]
GIOVANNI_SIZE = 63  # GIOVANNI isch momentan Anatol sin teil
GIOVANNI_SCALE = 4.4
GIOVANNI_YOFFSET = 5
GIOVANNI_OFFSET = [25, 9]
GIOVANNI_DATA = [GIOVANNI_SIZE, GIOVANNI_SCALE, GIOVANNI_OFFSET]
BOSS_SIZE = 114  # Boss is vincent will er mich bestoche hät
BOSS_SCALE = 2.2
BOSS_YOFFSET = 0
BOSS_OFFSET = [35, 15]
BOSS_DATA = [BOSS_SIZE, BOSS_SCALE, BOSS_OFFSET]
DISABLO_SIZE = 89
DISABLO_SCALE = 4.5
DISABLO_YOFFSET = 0
DISABLO_OFFSET = [37, 26]
DISABLO_DATA = [DISABLO_SIZE, DISABLO_SCALE, DISABLO_OFFSET]

# load a background image
bg_image = [0, 0, 0, 0, 0]
bg_image[0] = pygame.image.load("assets/images/background/template background.png").convert_alpha()
bg_image[1] = pygame.image.load("assets/images/background/Rick.png").convert_alpha()
bg_image[2] = pygame.image.load("assets/images/background/desertbackground.png").convert_alpha()



# load spritesheets
stickman_sheet = pygame.image.load("assets/images/character tom/Spritesheet.png").convert_alpha()
GIOVANNI_sheet = pygame.image.load("assets/images/character anatol/GiovanniGiorgioSpritesheet.png").convert_alpha()
BOSS_sheet = pygame.image.load("assets/images/character vincent/boss.png").convert_alpha()
DISABLO_sheet = pygame.image.load("assets/images/character noah/sheet.png").convert_alpha()

# define number of frames per animation
STICKMAN_ANIMATION_STEPS = [2, 8, 1, 7, 7, 3, 7]
GIOVANNI_ANIMATION_STEPS = [5, 6, 1, 5, 6, 2, 8]
BOSS_ANIMATION_STEPS = [2, 2, 1, 6, 3, 2, 6]
DISABLO_ANIMATION_STEPS = [4, 7, 2, 5, 4, 2, 10]

# preparing for a general character selection menu
GIOVANNI_CHARACTER_DATA = [2, 200, SCREEN_HEIGHT - 400, True, GIOVANNI_DATA, GIOVANNI_sheet, GIOVANNI_ANIMATION_STEPS,
                           GIOVANNI_YOFFSET]
STICKMAN_CHARACTER_DATA = [1, SCREEN_WIDTH - 280, SCREEN_HEIGHT - 400, False, STICKMAN_DATA, stickman_sheet,
                           STICKMAN_ANIMATION_STEPS, 0]
VINCENT_CHARACTER_DATA = [0, 0, 0, 0, BOSS_DATA, BOSS_sheet, BOSS_ANIMATION_STEPS, 0]
DISABLO_CHARACTER_DATA = [0, 0, 0, 0, DISABLO_DATA, DISABLO_sheet, DISABLO_ANIMATION_STEPS, DISABLO_YOFFSET]
MASTER_CHARACTER_DATA = [STICKMAN_CHARACTER_DATA, GIOVANNI_CHARACTER_DATA, VINCENT_CHARACTER_DATA,
                         DISABLO_CHARACTER_DATA]


# letting user pick character
# USER_1 = int(input("Player one choose Character: 0 = Stickman, 1= Pizza Guy\n")) shifted to the top for convenience


# function to display background image
def draw_bg(map):
    # if background image needs to be stretched
    scaled_bg = pygame.transform.scale(bg_image[map], (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))


# creating health bars
def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE,
                     (x - 4, y - 4, 408, 38))  # the following three lines are only for aesthetic UI purposes
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))


def main():
    global quit
    quit = False

    pygame.init()
    while not quit:
        characterInfo = showWelcomeAnimation()
        print("showWelcomeAnimation OK")
        finishInfo = mainGame(characterInfo)
        print("finishInfo OK")
        quit = finishInfo["quit"]

        showGameOverScreen(finishInfo)

    pygame.quit()


def showGameOverScreen(finishInfo):
    pass


def reset(characterInfo):
    global fighter_1, fighter_2, map
    # create fighters instances
    USER_1 = characterInfo[0]
    USER_2 = characterInfo[1]
    map = characterInfo[2]
    if USER_1 and USER_2 == -1:
        pygame.quit()
    fighter_1 = Fighter(1, 200, SCREEN_HEIGHT - 400, False, MASTER_CHARACTER_DATA[USER_1][4],
                        MASTER_CHARACTER_DATA[USER_1][5], MASTER_CHARACTER_DATA[USER_1][6],
                        MASTER_CHARACTER_DATA[USER_1][7])
    fighter_2 = Fighter(2, SCREEN_WIDTH - 280, SCREEN_HEIGHT - 400, True, MASTER_CHARACTER_DATA[USER_2][4],
                        MASTER_CHARACTER_DATA[USER_2][5], MASTER_CHARACTER_DATA[USER_2][6],
                        MASTER_CHARACTER_DATA[USER_2][7])  # the GIOVANNI ones are GIOVANNI place holders for it to work

    # lobal  last_count_update, oder vlcht in showWelcomeAnimation
    last_count_update = pygame.time.get_ticks()
    intro_count = 3
    while intro_count > 0:
        # anfangsbildschirm anzeigen, mit beiden personen oben.

        if (pygame.time.get_ticks() - last_count_update) >= 1000:
            intro_count -= 1
            last_count_update = pygame.time.get_ticks()
            print(intro_count)


def mainGame(characterInfo):
    # create game loop (never load sprites/images withhin gameloop if background)
    reset(characterInfo)
    death_counter = 0

    while True:
        draw_bg(map)

        # draw healthbars/show player stats
        draw_health_bar(fighter_1.health, 20, 20)
        draw_health_bar(fighter_2.health, SCREEN_WIDTH - 420, 20)

        # finisch if someone is dead
        if fighter_2.health * fighter_2.health == 0:
            death_counter += 1
        if death_counter >= FPS * 2:  # 2 second dead
            return {"quit": False}

        # move fighters
        fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2)
        fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1)

        # update fighter animation
        fighter_1.update(screen, fighter_2)
        fighter_2.update(screen, fighter_1)

        # draw the character instances
        fighter_1.draw(screen)
        fighter_2.draw(screen)

        # quit?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return {"quit": True}

        # display update
        pygame.display.update()

        clock.tick(FPS)


if __name__ == '__main__':
    main()
    print("S'Programm isch guet z'endi cho Jungs")
