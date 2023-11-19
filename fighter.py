import pygame

floorheight = 110


class Fighter():
    def __init__(self, player, x, y, flip, data, sprite_sheet, animation_steps):
        self.player = player
        self.size = data[0]  # goes to the first item of the list
        self.image_scale = data[1]  # takes second data fed in by STICKMAN_DATA/ TEMPORARY_DATA
        self.offset = data[2]
        self.flip = flip
        self.animation_list = self.load_images(sprite_sheet, animation_steps)
        self.action = 0  # 0 idle, 1 death, 2 fall, 3 idle, 4 jump, 5 run, 6 take hit| currently for stickman, see line +- 40 in main.py
        self.frame_index = 0
        self.image = self.animation_list[self.action][self.frame_index]  # as frame index increases, the animation progresses
        self.update_time = pygame.time.get_ticks()
        self.rect = pygame.Rect((x, y, 80, 180))
        self.vel_y = 0
        self.running = False
        self.jump = False  # set jump to false when spawning
        self.attacking = False
        self.attack_type = 0
        self.attack_cooldown = 0
        self.hit = False
        self.health = 100
        self.alive = True

    def load_images(self, sprite_sheet, animation_steps):
        # extract images from spritesheet
        animation_list = []  # create master list that contains all animation frames
        for y, animation in enumerate(animation_steps):  # here y tracks the number of loops that have passed
            temp_img_list = []
            for x in range(animation):
                temp_img = sprite_sheet.subsurface(x * self.size, y * self.size, self.size,
                                                   self.size)  # size of each square sprite
                temp_img_list.append(
                    pygame.transform.scale(temp_img, (self.size * self.image_scale, self.size * self.image_scale)))
            animation_list.append(temp_img_list)
        return animation_list

    def move(self, screen_width, screen_height, surface, target):
        SPEED = 10
        GRAVITY = 2
        dx = 0
        dy = 0
        self.running = False
        self.attack_type = 0

        # take inputs
        key = pygame.key.get_pressed()

        # make sure the player is only able to move while not attacking -> will fix later but for the moment follow the tutorial
        if self.alive == True:
            #check player 1 controls
            if self.player == 1:
                # movement
                if key[pygame.K_a]:
                    dx = -SPEED
                    self.running = True
                if key[pygame.K_d]:
                    dx = SPEED
                    self.running = True

                # jumping
                if key[pygame.K_w] and self.jump == False:
                    self.vel_y = -40
                    self.jump = True
                # lmao fuck following the tutorial ill do it myself -> see line 24
                if self.attacking == False:
                    # attack inputs
                    if key[pygame.K_r] or key[pygame.K_t]:
                        self.attack(surface, target)

                        # determine the actual input / attack type
                        if key[pygame.K_r]:
                            self.attack_type = 1
                        if key[pygame.K_t]:
                            self.attack_type = 2
            #check player 2 controls
            if self.player == 2:
                # movement
                if key[pygame.K_LEFT]:
                    dx = -SPEED
                    self.running = True
                if key[pygame.K_RIGHT]:
                    dx = SPEED
                    self.running = True

                # jumping
                if key[pygame.K_UP] and self.jump == False:
                    self.vel_y = -40
                    self.jump = True
                # lmao fuck following the tutorial ill do it myself -> see line 24
                if self.attacking == False:
                    # attack inputs
                    if key[pygame.K_KP1] or key[pygame.K_KP2]:
                        self.attack(surface, target)

                        # determine the actual input / attack type
                        if key[pygame.K_KP1]:
                            self.attack_type = 1
                        if key[pygame.K_KP2]:
                            self.attack_type = 2

        # add gravity
        self.vel_y += GRAVITY
        dy += self.vel_y

        # Screen borders
        # go to the far left of the screen
        if self.rect.left + dx < 0:
            dx = 0 - self.rect.left
        # go to the far right
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - floorheight:
            self.vel_y = 0
            dy = screen_height - floorheight - self.rect.bottom
            self.jump = False

        # ensure players are facing each other
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True

        #apply attack cooldown
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

        # update player position
        self.rect.x += dx
        self.rect.y += dy

    #create update method -> handles animation updates
    def update(self):
        #check which action is being performed, the order of the checks is relevant, although not yet grasped
        if self.health <= 0:
            self.health = 0
            self.alive = False
            self.update_action(6) #death
        elif self.hit == True:
            self.update_action(5) # being hit
        elif self.attacking == True:
            if self.attack_type == 1:
                self.update_action(3) #attack 1
            elif self.attack_type == 2:
                self.update_action(4) #atack 2
        elif self.jump == True:
            self.update_action(2) #jump
        elif self.running == True:
            self.update_action(1)#consider the sprite sheet structure, 1= run
        else:
            self.update_action(0) #because animations are of different lengths, we need help function, see below attack method, 0 = idle

        animation_cooldown = 70 #pygame tick are in milliseconds
        #update image
        self.image = self.animation_list[self.action][self.frame_index]
        #check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        #check whether animation has finished
        if self.frame_index >= len(self.animation_list[self.action]):
            #if the player is dead, end animation
            if self.alive == False:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0
                #check if an attack was executed
                if self.action == 3 or self.action == 4:
                    self.attacking = False
                    self.attack_cooldown = 20
                #check if damage was taken
                if self.action == 5:
                    self.hit = False
                    #if player was performing attack while being hit, stop attack
                    self.attacking = False
                    self.attack_cooldown = 20


    # create a attacking hitbox infront of the player
    def attack(self, surface, target):
        if self.attack_cooldown == 0:
            self.attacking = True
            attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y,
                                         2 * self.rect.width,
                                         self.rect.height)  # the added self.flip argument line equals 0, if the statement is false, therefore the default direction stays righthand
            if attacking_rect.colliderect(target.rect):  # introduce generic variable so the target can be defined for each fighter
                target.health -= 10
                target.hit = True
            pygame.draw.rect(surface, (0, 255, 0), attacking_rect)

    def update_action(self, new_action):
        #check whether if the new action differs from previous one
        if new_action != self.action:
            self.action = new_action
            #reset the frame index
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()


    def draw(self, surface):
        #reuse the self.flip variable
        img = pygame.transform.flip(self.image, self.flip, False)
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
        surface.blit(img, (self.rect.x - (self.offset[0] * self.image_scale), self.rect.y - (self.offset[1] * self.image_scale)))
