import pygame
from pygame.sprite import Group
from Settings import Settings
from bullet import Bullet
from ship import Ship
import game_functions

def rungame():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen, ai_settings)
    bullets = Group()
    
    while True:
        game_functions.check_events(ship,ai_settings,screen,bullets)
        ship.update()
        game_functions.update_bullet(bullets)
        game_functions.update_screen(ai_settings,screen,ship,bullets)
rungame()