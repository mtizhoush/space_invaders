import pygame
from pygame.sprite import Sprite

class AlienBullet(Sprite):

    def __init__(self, ai_settings, screen, alien):
        super(AlienBullet, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, ai_settings.alien_bullet_width, ai_settings.alien_bullet_height)
        self.rect.centerx = alien.rect.centerx
        self.rect.bottom = alien.rect.bottom

        self.y = float(self.rect.y)

        self.color = ai_settings.alien_bullet_color
        self.speed = ai_settings.alien_bullet_speed

    def update(self):
        #Update decimal position of bullet
        self.y += self.speed
        #Update the rect position
        self.rect.y = self.y

    def draw_alien_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)