import imp
import sys
from tkinter.tix import Tree
import pygame
from bullet import Bullet

def check_keydown_events(event,ship,ai_settings,screen,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
        
def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship,ai_settings,screen,bullets):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event,ship,ai_settings,screen,bullets)
            elif event.type == pygame.KEYUP:
                check_keyup_events(event,ship)
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            #     ship.rect.centerx += 1
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            #     ship.rect.centerx -= 1

def update_screen(ai_settings,screen,ship,bullets):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    pygame.display.flip()

def update_bullet(bullets):
    bullets.update()
    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        # print(len(bullets))

def fire_bullet(ai_settings, screen, ship, bullets):
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
