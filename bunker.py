import pygame
from pygame.sprite import Sprite

class Bunker(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ai_settings, screen):
        super(Bunker, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #Load the bunker image and set its rect attribute
        self.image = pygame.image.load('images/bunker.gif')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start each new bunker near the bottom of the screen above the ship
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Store the bunkers exaxt position
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        self.blitme()