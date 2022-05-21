import sys
import os
import pytest
import pygame
sys.path.append('..')
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import import_abc
from ship import Ship
from Settings import Settings

@pytest.fixture
def create_ship():
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    new_ship = Ship(screen,ai_settings)
    # return [new_ship,screen]
    return new_ship


def test_ship_init_params(create_ship):
    # assert  create_ship[0].rect.centerx == create_ship[0].screen_rect.centerx
    # assert  create_ship[0].rect.bottom == create_ship[0].screen_rect.bottom

    assert  create_ship.rect.centerx == create_ship.screen_rect.centerx
    assert  create_ship.center == create_ship.rect.centerx
    assert  create_ship.rect.bottom == create_ship.screen_rect.bottom
    assert  create_ship.moving_right == False
    assert  create_ship.moving_left == False

def test_ship_center_ship(create_ship):
    create_ship.center_ship()
    assert create_ship.center == create_ship.screen_rect.centerx

@pytest.mark.parametrize("moving_right, rect_right, screen_rect_right, moving_left, rect_left",[(True,53,15,True,5)])
def test_ship_update(create_ship,moving_right, rect_right, screen_rect_right, moving_left, rect_left):
    create_ship.rect.right = rect_right
    create_ship.screen_rect.right = screen_rect_right
    create_ship.rect.left = rect_left
    create_ship.moving_right = moving_right
    create_ship.moving_left = moving_left
    create_ship.update()
    
    if create_ship.moving_right and create_ship.rect.right < create_ship.screen_rect.right:
        assert create_ship.center == create_ship.center + create_ship.ai_settings.ship_speed_factor
    if create_ship.moving_left and create_ship.rect.left > 0:
        assert create_ship.center == create_ship.center - create_ship.ai_settings.ship_speed_factor
    
    assert create_ship.rect.centerx == create_ship.center



# def test_greek():
#     assert import_abc.r.geeks == "child class"
