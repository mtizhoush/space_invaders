import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ai_settings, screen, type):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.type = type

        #Load the alien1 image and set its rect attribute
        self.images = []
        self.images.append(pygame.image.load('images/alien1.gif'))
        self.images.append(pygame.image.load('images/alien11.gif'))
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()

        #Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the alien's exaxt position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.image2, self.rect)

    def check_edges(self):
        """Return true if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        if pygame.time.get_ticks() % 150 == 0:
            self.index += 1
            if self.index >= len(self.images):
                    self.index = 0
            self.image = self.images[self.index]

        """Move the alien right of left"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x


class Alien2(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ai_settings, screen, type):
        super(Alien2, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.type = type

        #Load the alien1 image and set its rect attribute
        self.image = pygame.image.load('images/alien2.gif')
        self.rect = self.image.get_rect()

        #Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the alien's exaxt position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return true if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right of left"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

class Alien3(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ai_settings, screen, type):
        super(Alien3, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.type = type

        #Load the alien1 image and set its rect attribute
        self.image = pygame.image.load('images/alien3.gif')
        self.rect = self.image.get_rect()

        #Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the alien's exaxt position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return true if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right of left"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
