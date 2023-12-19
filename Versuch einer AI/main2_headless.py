import pygame
from figther_headless import Fighter
from function_q import paramsToState, calculateDeltaHealth, Q_jump, Q_walk, Q_attack, alpha, gamma
import pickle

# AI leans with random move
#letting user pick character
USER_1 = 0 # int(input("Player one choose Character: 0 = Stickman, 1= Pizza Guy, 2 = Vincent\n"))
USER_2 = 0 # int(input("Player two choose Character: 0 = Stickman, 1= Pizza Guy, 2 = Vincent\n"))

gameCounter = 0
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
intro_count = 0
last_count_update = pygame.time.get_ticks()



# define fighter variables
STICKMAN_SIZE = 162  # character size withhin spritesheet
STICKMAN_SCALE = 4
STICKMAN_OFFSET = [72, 56] #find through testing
STICKMAN_DATA = [STICKMAN_SIZE, STICKMAN_SCALE, STICKMAN_OFFSET, 0]
GIOVANNI_SIZE = 63 #GIOVANNI isch momentan Anatol sin teil
GIOVANNI_SCALE = 4.4
GIOVANNI_YOFFSET = 5
GIOVANNI_OFFSET = [25, 9]
GIOVANNI_DATA = [GIOVANNI_SIZE, GIOVANNI_SCALE, GIOVANNI_OFFSET]
BOSS_SIZE = 114 #Boss is vincent will er mich bestoche hät
BOSS_SCALE = 2.2
BOSS_YOFFSET = 0
BOSS_OFFSET = [35, 15]
BOSS_DATA = [BOSS_SIZE, BOSS_SCALE, BOSS_OFFSET]

# load a background image
bg_image = pygame.image.load("assets/images/background/template background.png").convert_alpha()

# load spritesheets
stickman_sheet = pygame.image.load("assets/images/character tom/Spritesheet.png").convert_alpha()
GIOVANNI_sheet = pygame.image.load(
    "assets/images/character anatol/GiovanniGiorgioSpritesheet.png").convert_alpha()
BOSS_sheet = pygame.image.load("assets/images/character vincent/boss.png").convert_alpha()

# define number of frames per animation
STICKMAN_ANIMATION_STEPS = [2, 8, 1, 7, 7, 3, 7]
GIOVANNI_ANIMATION_STEPS = [5, 6, 1, 5, 6, 2, 8]
BOSS_ANIMATION_STEPS = [2, 2, 1, 6, 3, 2, 6]

#preparing for a general character selection menu
GIOVANNI_CHARACTER_DATA = [2, 200, SCREEN_HEIGHT-400, True,  GIOVANNI_DATA, GIOVANNI_sheet,GIOVANNI_ANIMATION_STEPS, GIOVANNI_YOFFSET]
STICKMAN_CHARACTER_DATA = [1, SCREEN_WIDTH-280 , SCREEN_HEIGHT-400, False, STICKMAN_DATA, stickman_sheet, STICKMAN_ANIMATION_STEPS, 0]
VINCENT_CHARACTER_DATA = [0, 0, 0 , 0, BOSS_DATA, BOSS_sheet, BOSS_ANIMATION_STEPS, 0]
MASTER_CHARACTER_DATA = [STICKMAN_CHARACTER_DATA, GIOVANNI_CHARACTER_DATA, VINCENT_CHARACTER_DATA]



#letting user pick character
#USER_1 = int(input("Player one choose Character: 0 = Stickman, 1= Pizza Guy\n")) shifted to the top for convenience


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



def main(onGameover):
    global quit
    quit = False

    pygame.init()
    while not quit:
        #characaterInfo = showWelcomeAnimation(
        # )
        characaterInfo = {}
        finishInfo = mainGame(characaterInfo)
        print("finishInfo OK")
        quit = finishInfo["quit"]
        #onGameover(finishInfo)
        print(gameCounter)
        #showGameOverScreen(finishInfo)

    pygame.quit()

def showWelcomeAnimation():
    pass


def showGameOverScreen(finishInfo):
    pass

def reset(characaterInfo):
    global fighter_1, fighter_2
    # create fighters instances
    fighter_1 = Fighter(1, 400, SCREEN_HEIGHT-400, False ,MASTER_CHARACTER_DATA[USER_1][4], MASTER_CHARACTER_DATA[USER_1][5],MASTER_CHARACTER_DATA[USER_1][6],MASTER_CHARACTER_DATA[USER_1][7])
    fighter_2 = Fighter(2, 450 , SCREEN_HEIGHT-400, True ,MASTER_CHARACTER_DATA[USER_2][4], MASTER_CHARACTER_DATA[USER_2][5],MASTER_CHARACTER_DATA[USER_2][6],MASTER_CHARACTER_DATA[USER_2][7])  # the GIOVANNI ones are GIOVANNI place holders for it to work
    pygame.time.delay(1000)


oldState_1 = "0"
oldState_2 = "0"

def mainGame(characaterInfo):
    global oldMove_1, oldMove_2, oldState_1, oldState_2, gameCounter

    reset(characaterInfo)

    # create game loop (never load sprites/images withhin gameloop if background)
    death_counter = 0


    while True:
        gameCounter += 1
        #rrrrrrrrrrrrrrrrrrrrraus
        #draw_bg()

        # draw healthbars/show player stats
        # rrrrrrrrrrrrrrrrrrrrrrrrrrrrraus
        #draw_health_bar(fighter_1.health, 20, 20)
        #draw_health_bar(fighter_2.health, SCREEN_WIDTH - 420, 20)

        # finisch if someone is dead
        if fighter_1.health * fighter_2.health == 0:
            return {"quit": False}


        # update mov' 'n' state
        movement_1 = fighter_1.shouldEmulateKeyPress() #(fighter_1.params,fighter_2.params)
        movement_2 = fighter_2.shouldEmulateKeyPress() #fighter_2.params,fighter_1.params)
        state_1 = paramsToState(fighter_1.update_params(), fighter_2.update_params())
        state_2 = paramsToState(fighter_2.update_params(), fighter_1.update_params())
        delta_health_1 = calculateDeltaHealth(fighter_1.update_params(), fighter_2.update_params())
        delta_health_2 = - delta_health_1

        # move fighters
        fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2, movement_1)
        fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1, movement_2)
        try:
            #print(int(state_1.split("_")[2]))
            # reward =  (for the time) compare Δhealth
            health_1 = (int(state_1.split("_")[2]) - int(oldState_1.split("_")[2])) * 1000 # pos good, neg bad

        except IndexError:
            health_1 = 0



        reward_1 = health_1
        if reward_1 == 0:
            reward_1 = -1
         # could be more complex.
        reward_2 = - reward_1 # could be more complex.



        # q figther_1
        prevReward_walk_1 = Q_walk[oldState_1]
        prevReward_jump_1 = Q_jump[oldState_1]
        prevReward_attack_1 = Q_attack[oldState_1]
        try:
            #print((1 - alpha) * prevReward_walk_1[oldMove_1["walk"]] + alpha * (reward_1 + max(prevReward_walk_1)))
            prevReward_walk_1[oldMove_1["walk"]] = (1 - alpha) * prevReward_walk_1[oldMove_1["walk"]] + alpha * (reward_1 + max(prevReward_walk_1))
            prevReward_jump_1[oldMove_1["jump"]] = (1 - alpha) * prevReward_jump_1[oldMove_1["jump"]] + alpha * (reward_1 + max(prevReward_jump_1))
            prevReward_attack_1[oldMove_1["attack"]] = (1 - alpha) * prevReward_attack_1[oldMove_1["attack"]] + alpha * (reward_1 + max(prevReward_attack_1))

            Q_walk[oldState_1] = prevReward_walk_1
            Q_jump[oldState_1] = prevReward_jump_1
            Q_attack[oldState_1] = prevReward_attack_1


        except NameError:
            pass


        # q fighter_2
        prevReward_walk_2 = Q_walk[oldState_2]
        prevReward_jump_2 = Q_jump[oldState_2]
        prevReward_attack_2 = Q_attack[oldState_2]

        try:
            prevReward_walk_2[oldMove_2["walk"]] = (1 - alpha) * prevReward_walk_2[oldMove_2["walk"]] + alpha * (reward_2 + max(prevReward_walk_2))
            prevReward_jump_2[oldMove_2["jump"]] = (1 - alpha) * prevReward_jump_2[oldMove_2["jump"]] + alpha * (reward_2 + max(prevReward_jump_2))
            prevReward_attack_2[oldMove_2["attack"]] = (1 - alpha) * prevReward_attack_2[oldMove_2["attack"]] + alpha * (reward_2 + max(prevReward_attack_2))

            Q_walk[oldState_2] = prevReward_walk_2
            Q_jump[oldState_2] = prevReward_jump_2
            Q_attack[oldState_2] = prevReward_attack_2

        except NameError:
            pass

        # save q

        if gameCounter % 25000000 == 0: # früher 10 mal mehr
            s = str(alpha) + "_" + str(gamma)
            with open("Q/" + str(gameCounter) + "_walk_" + s + ".pickle", "wb") as file:
                pickle.dump(dict(Q_walk), file)
            with open("Q/" + str(gameCounter) + "_jump_" + s + ".pickle", "wb") as file:
                pickle.dump(dict(Q_jump), file)
            with open("Q/" + str(gameCounter) + "_attack_" + s + ".pickle", "wb") as file:
                pickle.dump(dict(Q_attack), file)

            if gameCounter == 100000000:
                return {"quit": True}




        # new to old
        oldMove_1 = movement_1
        oldMove_2 = movement_2

        oldState_1 = state_1
        oldState_2 = state_2

        oldDelta_health_1 = delta_health_1
        oldDelta_health_2 = delta_health_2


        # update fighter animation
        fighter_1.update(screen, fighter_2)
        fighter_2.update(screen, fighter_1)


        # draw the character instances
        # rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrraus
        #fighter_1.draw(screen)
        #fighter_2.draw(screen)

        # quit?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                s = str(alpha) + "_" + str(gamma)
                with open("Q/" + str(gameCounter) + "_walk_" + s + ".pickle", "wb") as file:
                    pickle.dump(dict(Q_walk), file)
                with open("Q/" + str(gameCounter) + "_jump_" + s + ".pickle", "wb") as file:
                    pickle.dump(dict(Q_jump), file)
                with open("Q/" + str(gameCounter) + "_attack_" + s + ".pickle", "wb") as file:
                    pickle.dump(dict(Q_attack), file)
                return {"quit":True}

        # display update
        #pygame.display.update()
        #clock.tick(FPS)



if __name__ == '__main__':
    main([0])
    print("S'Programm isch guet z'endi cho Jungs")
