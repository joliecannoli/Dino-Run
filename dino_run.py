import pygame 
import os

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

    def __init__ (self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING
        
        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
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
        pass

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

def main():
    run = True 
    clock = pygame.time.Clock()
    player = Dinosaur()

    while run: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        color = (182, 198, 222)
        SCREEN.fill(color)
        userInput = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(userInput)

        clock.tick(30)
        pygame.display.update()

main() 