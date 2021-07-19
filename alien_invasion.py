import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #инициализуется игра и создается объект экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen,ai_settings)
    #создание группы для хранения пуль
    bullets = Group()

    #запуск основного цикла
    while True:
        #отслеживание клавиатуры клавиш и мыши
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)

        gf.update_screen(ai_settings, screen, ship, bullets)



run_game()