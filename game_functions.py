import sys
import pygame

def check_events(ship):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    ship.rect.centerx += 1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                ship.rect.centerx -= 1
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            #     ship.rect.centerx += 1
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            #     ship.rect.centerx -= 1

def update_screen(ai_settings,screen,ship):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()
