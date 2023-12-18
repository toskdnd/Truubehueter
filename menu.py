import pygame
import button
def showWelcomeAnimation():
    pygame.init()
    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    def loading_screen():
        draw_text(f"game will start soon...", title_font, TEXT_COL, 160, 300)
        screen.blit(studioLogo,(800,200))

    def map_select():
        pygame.draw.rect(screen, (52, 40, 80), (0, 0, 1280, 720))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mapSelect = False
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mapSelect = False
                    main_menu = True
                if event.key == pygame.K_0:
                    UserID[2] = 0
                    mapSelect = False
                    characterSelect1 = True
                    print("1")

                elif event.key == pygame.K_1:
                    UserID[2] = 1
                    mapSelect = False
                    characterSelect1 = True
                    print("2")

                elif event.key == pygame.K_2:
                    UserID[2] = 2
                    mapSelect = False
                    characterSelect1 = True
                    print("3")

                elif event.key == pygame.K_3:
                    UserID[2] = 3
                    mapSelect = False
                    characterSelect1 = True
                    print("4")
                else:
                    print("niente")




    #define game variables
    main_menu = False
    First = True
    mapSelect = False
    characterSelect1 = False
    characterSelect2 = False
    UserID = [-1,-1,-1]

    #image load
    studioLogoRaw = pygame.image.load("assets/images/Logo.png").convert_alpha()
    studioLogo = pygame.transform.scale_by(studioLogoRaw,5)




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
            #loading screen
            screen.fill((52,40,80))

            draw_text("Welcome to Yeetfighter", title_font, TEXT_COL, 160, 400)
            draw_text("press any key to continue...", subtitle_font, TEXT_COL, 160, 490)
            for i in range(0,1):
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        main_menu = True
                        First = False
                    elif event.type == pygame.QUIT:
                        First = False
                        run = False
        if main_menu == True:
            screen.fill((52,40,80))
            pygame.draw.rect(screen,(52,40,80), (0,0,1280,720))
            draw_text("menu", title_font,TEXT_COL,160,400)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        characterSelect1 = True
                        main_menu = False
                    if event.key == pygame.K_ESCAPE:
                        main_menu = False
                        First = True
                    if event.type == pygame.QUIT:
                        run = False

        if (mapSelect):
            map_select()

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
                        mapSelect = True
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
                    if event.key == pygame.K_ESCAPE:
                        characterSelect2 = False
                        characterSelect1 = True
                    if event.key == pygame.K_0:
                        UserID[1] = 0
                        characterSelect2 = False
                        pygame.draw.rect(screen, (52, 40, 80), (0, 0, 1280, 720))
                        loading_screen()
                        run = False
                        print("1")

                    elif event.key == pygame.K_1:
                        UserID[1] = 1
                        characterSelect2 = False
                        pygame.draw.rect(screen, (52, 40, 80), (0, 0, 1280, 720))
                        loading_screen()
                        run = False
                        print("2")

                    elif event.key == pygame.K_2:
                        UserID[1] = 2
                        characterSelect2 = False
                        pygame.draw.rect(screen, (52, 40, 80), (0, 0, 1280, 720))
                        loading_screen()
                        run = False
                        print("3")

                    elif event.key == pygame.K_3:
                        UserID[1] = 3
                        characterSelect2 = False
                        pygame.draw.rect(screen, (52, 40, 80), (0, 0, 1280, 720))
                        loading_screen()
                        run = False
                        print("4")
                    else:
                        print("niente")


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        pygame.display.update()

    return UserID


