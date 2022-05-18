import pygame
from pygame.sprite import Group
from Settings import Settings
from bullet import Bullet
from ship import Ship
from game_stats import GameStats
import game_functions

def rungame():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Create an instance to store game statistics.
    stats = GameStats(ai_settings)
    ship = Ship(screen, ai_settings)
    bullets = Group()
    aliens = Group()

    game_functions.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        game_functions.check_events(ship, ai_settings, screen, bullets)
        ship.update()
        game_functions.update_bullet(ai_settings, screen, ship, aliens, bullets)
        game_functions.update_aliens(ai_settings, stats, ship, aliens)
        game_functions.update_screen(ai_settings, screen,ship, bullets,aliens)
rungame()