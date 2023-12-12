import pygame
import button
def showWelcomeAnimation():
    pygame.init()
    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    #define game variables
    game_paused = False
    First = True
    characterSelect1 = False
    characterSelect2 = False
    UserID = [1, 2]


    #define fonts
    title_font = pygame.font.SysFont("arialblack", 40)
    subtitle_font = pygame.font.SysFont("arialblack", 25)

    #define color
    TEXT_COL = (255, 255, 255)


    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Splash Screen")

    run = True
    while run:

        if (First):
            screen.fill((52, 40, 80))
            draw_text("Welcome to Yeetfighter", title_font, TEXT_COL, 160, 400)
            draw_text("press any key to continue...", subtitle_font, TEXT_COL, 160, 490)
            for i in range(0,1):
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        game_paused = True
                        First = False
                    elif event.type == pygame.QUIT:
                        First = False
                        run = False
        if game_paused == True:
            screen.fill((52,40,80))
            pygame.draw.rect(screen,(52,40,80), (0,0,1280,720))
            draw_text("menu", title_font,TEXT_COL,160,400)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        characterSelect1 = True
                        game_paused = False
                    if event.key == pygame.K_ESCAPE:
                        game_paused = False
                        First = True
                    if event.type == pygame.QUIT:
                        run = False
        if characterSelect1 == True:
            pygame.draw.rect(screen, (52, 40, 80), (0, 0, 1280, 720))
            draw_text(f"Player 1 choose character", title_font,TEXT_COL,160,300)
            draw_text("ligmastickma(0) giovannigiorgio(1) boss(2) disablo(3)",title_font,TEXT_COL,50,400)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    characterSelect1 = False
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        characterSelect1 = False
                        game_paused = True
                    if event.key == pygame.K_0:
                        UserID[0] = 0
                        characterSelect1 = False
                        characterSelect2 = True
                        print("1")

                    elif event.key == pygame.K_1:
                        UserID[0] = 1
                        characterSelect1 = False
                        characterSelect2 = True
                        print("2")

                    elif event.key == pygame.K_2:
                        UserID[0] = 2
                        characterSelect1 = False
                        characterSelect2 = True
                        print("3")

                    elif event.key == pygame.K_3:
                        UserID[0] = 3
                        characterSelect1 = False
                        characterSelect2 = True
                        print("4")
                    else:
                        print("niente")
        if characterSelect2 == True:
            pygame.draw.rect(screen, (52, 40, 80), (0, 0, 1280, 720))
            draw_text(f"Player 2 choose character", title_font, TEXT_COL, 160, 300)
            draw_text("ligmastickma(0) giovannigiorgio(1) boss(2) disablo(3)", title_font, TEXT_COL, 50, 400)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    characterSelect2 = False
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_0:
                        UserID[1] = 0
                        characterSelect2 = False
                        pygame.draw.rect(screen, (52, 40, 80), (0, 0, 1280, 720))
                        draw_text(f"game will start soon", title_font, TEXT_COL, 160, 300)
                        run = False
                        print("1")

                    elif event.key == pygame.K_1:
                        UserID[1] = 1
                        characterSelect2 = False
                        pygame.draw.rect(screen, (52, 40, 80), (0, 0, 1280, 720))
                        draw_text(f"game will start soon", title_font, TEXT_COL, 160, 300)
                        run = False
                        print("2")

                    elif event.key == pygame.K_2:
                        UserID[1] = 2
                        characterSelect2 = False
                        pygame.draw.rect(screen, (52, 40, 80), (0, 0, 1280, 720))
                        draw_text(f"game will start soon", title_font, TEXT_COL, 160, 300)
                        run = False
                        print("3")

                    elif event.key == pygame.K_3:
                        UserID[1] = 3
                        characterSelect2 = False
                        pygame.draw.rect(screen, (52, 40, 80), (0, 0, 1280, 720))
                        draw_text(f"game will start soon", title_font, TEXT_COL, 160, 300)
                        run = False
                        print("4")
                    else:
                        print("niente")


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        pygame.display.update()

    return UserID

