import pygame
window_height = 1000
window_width = 800
MAP_BLUE=(0,162,232)
GREY=(119,118,110)
BLUE=(0,0,125)
BLACK=(0,0,0)

caption =  "Pacman"
pygame.display.set_caption(caption)
screen = pygame.display.set_mode([window_width, window_height])


start_text = "Press 1 to start"
high_scores_text = "Press 2 to see high scores"
options_text = "Press 3 to see options"
quit_text = "Press 4 to exit"