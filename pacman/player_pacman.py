import pygame
from constants import *

class Pacman(pygame.sprite.Sprite):

    def __init__(self, pacman_x, pacman_y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.pacman_vector_pos=pygame.Vector2(pacman_x, pacman_y)
        self.movement_speed=speed



    # def set_position(self):
    # sets the x and y position of pacman

    def load_image(self, pacman_image):

        #loads image based on  a signle arg
        self.pacman_image_var= pygame.image.load(pacman_image).convert_alpha()

       # self.pacman_image_var.convert_alpha()

    def draw_image(self):
        #blits image to the screen
        screen.blit(self.pacman_image_var, self.pacman_vector_pos)

    def player_rect_setup(self):
        self.pacman_rec = self.pacman_image_var.get_rect()

    def movement_get_position(self, delta_arg):

        keydown=pygame.key.get_pressed()
        if keydown[pygame.K_w]:
            self.pacman_vector_pos.y-=self.movement_speed * delta_arg


        if keydown[pygame.K_s]:
            self.pacman_vector_pos.y+=self.movement_speed * delta_arg

        if keydown[pygame.K_a]:
            self.pacman_vector_pos.x-=self.movement_speed * delta_arg

        if keydown[pygame.K_d]:
            self.pacman_vector_pos.x+=self.movement_speed * delta_arg





    # def load_image(self):
    # loads the png files
    # def draw_image(self):
    # draws the image to the screen
    # def player_teleport(self):
    # pacman teleports to x 1000 when x is negative

    # def collision_object(self):

    # when pacman collides with the food object the score increases and returns true


