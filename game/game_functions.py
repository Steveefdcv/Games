import sys
import pygame
from bullet import Bullet



def check_events(ai_settings, screen, ship, bullets):
	def check_keydown_events(event, ai_settings, screen, ship, bullets):
		if event.key == pygame.K_RIGHT:
			ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			ship.moving_left = True
		elif event.key == pygame.K_SPACE:
		    # Создание новой пули и включение ее в группу bullets.
		    new_bullet = Bullet(ai_settings, screen, ship)
		    bullets.add(new_bullet)
	def check_keyup_events(event, ship):
		if event.key == pygame.K_RIGHT:
		    ship.moving_right = False
		elif event.key == pygame.K_LEFT:
		    ship.moving_left = False
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		# Обработка нажатий.
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)

				

def update_screen(ai_settings, screen, ship, bullets):
	"""Обновляет изображения на экране и отображает новый экран."""
	# При каждом проходе цикла перерисовывается экран.
	screen.fill(ai_settings.bg_color)
    # Все пули выводятся позади изображений корабля и пришельцев.
	for bullet in bullets.sprites():
		bullet.draw_bullet()

	ship.blitme()
	# Отображение последнего прорисованного экрана.
	pygame.display.flip()