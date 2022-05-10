import sys
import pygame
from Settings import Settings
from ship import Ship
import game_functions

def rungame():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)
    
    while True:
        game_functions.check_events(ship)
        game_functions.update_screen(ai_settings,screen,ship)
rungame()