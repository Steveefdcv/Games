#-------------------------------------------------------------------------alien_invasion.py

import sys

import pygame

from settings import Settings

from ship import Ship

import game_functions as gf

from pygame.sprite import Group

def run_game():

	#---------------------------------------------------------------------Инициализирует игру и создает объект экрана.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	screen = pygame.display.set_mode((1200,800))
	pygame.display.set_caption("Alien Invasion")
	ship = Ship(ai_settings, screen)
	bg_color = (230, 230, 230)
	bullets = Group()


	#---------------------------------------------------------------------Запуск основного цикла игры.
	
	while True:
		screen.fill(bg_color)
		screen.fill(ai_settings.bg_color)
		ship.blitme()
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		bullets.update()
		gf.update_screen(ai_settings, screen, ship, bullets)

		#-----------------------------------------------------------------Отслеживание событий клавиатуры и мыши
		for event in pygame.event.get():
			gf.update_screen(ai_settings, screen, ship, bullets)
			if event.type == pygame.QUIT:
				sys.exit()

		#-----------------------------------------------------------------Отслеживание событий клавиатуры и мыши
		pygame.display.flip()

run_game()