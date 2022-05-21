import pygame
from pygame.sprite import Group
from Settings import Settings
from bullet import Bullet
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import game_functions

def rungame():
    pygame.init()
    # Start Alien Invasion in an active state.
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_settings, screen, "Play")
    # Create an instance to store game statistics.
    stats = GameStats(ai_settings)
    ship = Ship(screen, ai_settings)
    bullets = Group()
    aliens = Group()
    sb = Scoreboard(ai_settings, screen, stats)
    game_functions.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        game_functions.check_events(ship,ai_settings,screen,bullets, stats, play_button, aliens, sb)
        if stats.game_active:
            ship.update()
            game_functions.update_bullet(ai_settings, screen, ship, aliens, bullets, sb, stats)
            game_functions.update_aliens(ai_settings, stats, ship, aliens, screen, bullets, sb)
        game_functions.update_screen(ai_settings, stats, screen,ship, bullets,aliens,play_button,sb)
rungame()