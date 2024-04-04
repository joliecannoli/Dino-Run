import pygame 
import os
import random

pygame.init()
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100 
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

RUNNING = [pygame.image.load(os.path.join("pngs/dinosaur", "dino_run_1.png")),
           pygame.image.load(os.path.join("pngs/dinosaur", "dino_run_2.png"))]
JUMPING = pygame.image.load(os.path.join("pngs/dinosaur", "dino_jump.png"))
DUCKING = [pygame.image.load(os.path.join("pngs/dinosaur", "dino_duck_1.png")),
           pygame.image.load(os.path.join("pngs/dinosaur", "dino_duck_2.png"))]
                                          
SMALL_CACTUS = [pygame.image.load(os.path.join("pngs/cactus", "small_cactus_1.png")),
                pygame.image.load(os.path.join("pngs/cactus", "small_cactus_2.png")),
                pygame.image.load(os.path.join("pngs/cactus", "small_cactus_3.png"))]
LARGE_CACTUS = [pygame.image.load(os.path.join("pngs/cactus", "large_cactus_1.png")),
                pygame.image.load(os.path.join("pngs/cactus", "large_cactus_2.png")),
                pygame.image.load(os.path.join("pngs/cactus", "large_cactus_3.png"))]
BIRD = [pygame.image.load(os.path.join("pngs/bird", "bird_1.png")),
           pygame.image.load(os.path.join("pngs/bird", "bird_2.png"))]
TRACK = pygame.image.load(os.path.join("pngs/others", "track.png"))
CLOUDS = pygame.image.load(os.path.join("pngs/others", "cloud.png"))

class Dinosaur: 
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340 
    JUMP_VEL = 8.5

    def __init__ (self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING
        
        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    def update(self, userInput):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif userInput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -=0.8
        if self.jump_vel < - self.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

class Clouds:
    def __init__ (self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUDS
        self.width = self.image.get_width()

    def update(self):
        self.x -=game_speed 
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)
        
    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

def main():
    global game_speed, x_pos_bg, y_pos_bg
    run = True 
    clock = pygame.time.Clock()
    player = Dinosaur()
    cloud = Clouds()
    game_speed = 14
    x_pos_bg = 0
    y_pos_bg = 380

    def track():
        global x_pos_bg, y_pos_bg
        image_width = TRACK.get_width()
        SCREEN.blit(TRACK, (x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(TRACK, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    while run: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        color = (255, 255, 255)
        SCREEN.fill(color)
        userInput = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(userInput)
        track()

        cloud.draw(SCREEN)
        cloud.update()

        clock.tick(30)
        pygame.display.update()

main() 