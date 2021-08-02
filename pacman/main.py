import sys
import pygame
import player_pacman as pacman_object
from constants import *


class main(pygame.sprite.Sprite):
    pygame.init()
    pygame.font.init()

    def __init__(self, is_running):

        pygame.sprite.Sprite.__init__(self)
        self.player_pacman_instance = pacman_object.Pacman(200, 200, 100)

        # set screen, map and running variables
        self.game_start = False
        self.is_running = is_running
        self.screen = screen
        self.ticker = pygame.time.Clock()

    def GetDeltaTime(self):
        return self.ticker.tick() * 0.001

    def load_map_image(self, map_image):
        self.map = pygame.image.load(map_image).convert_alpha()

    def draw_map_image(self):
        self.screen.blit(self.map, (0, 0))

    def rect_map(self):
        self.map_rec = self.map.get_rect()
        print(self.map_rec)

    def map_mask(self):
        self.map_mask_var = pygame.mask.from_surface(self.map)
        return self.map_mask_var
# #https://stackoverflow.com/questions/20842801/how-to-display-text-in-pygame
    def Text(self,text_argument):
        self.font = pygame.font.SysFont(None, 24)
        self.render_text = self.font.render("%s" % text_argument, True, BLUE)

    def start_menu(self):
        screen.fill(BLACK)



        keydown = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

            if keydown[pygame.K_1]:
                self.game_start = True


        pygame.display.update()

    def game_loop(self):
        while self.is_running:

            if self.game_start:
                for event in pygame.event.get():

                    self.player_pacman_instance.movement_get_position(self.GetDeltaTime())
                    if event.type == QUIT:
                        sys.exit()

                self.screen.fill(GREY)
                self.load_map_image("images/PacmanMap.png")
                self.draw_map_image()
                self.map_mask()

                self.player_pacman_instance.load_image("images/pacman_open.png")
                self.player_pacman_instance.draw_image()
                self.player_pacman_instance.player_rect_setup()

                #  self.check_collision(self.map, self.player_pacman_instance.pacman_image_var)

                pygame.display.update()


            else:

                self.start_menu()


pacman_instance = main(True)
pacman_instance.game_loop()
