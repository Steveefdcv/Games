import pygame

class Ship():
    def __init__(self, ai_settings, screen):
    #---------------------------------------------------------------------Инициализирует корабль и задает его начальную позицию..
        self.screen = screen
        self.ai_settings = ai_settings
        # Загрузка изображения корабля и получение прямоугольника.

        self.image = pygame.image.load('images/spaceship_with_shadow (1) (1) (1).png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Каждый новый корабль появляется у нижнего края экрана.

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

        # Флаг перемещения
        self.moving_right = False

        self.moving_left = False
    
    def update(self):
        """Обновляет позицию корабля с учетом флага."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            if self.moving_right:
                self.rect.centerx += 1
                self.center += self.ai_settings.ship_speed_factor
                
        if self.moving_left and self.rect.left > 0:
            if self.moving_left:
                self.center -= self.ai_settings.ship_speed_factor
                self.rect.centerx -= 1
        
            
        self.rect.centerx = self.center
    def blitme(self):
        #---------------------------------------Рисует корабль в текущей позиции.

        self.screen.blit(self.image, self.rect)