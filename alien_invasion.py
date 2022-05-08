import sys
import pygame

def rungame():
    pygame.init()
    screen = pygame.display.set_mode((500,500))
    pygame.display.set_caption("Alien Invasion")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()

rungame()