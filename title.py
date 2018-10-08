import pygame.font

class Title():

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.image = pygame.image.load('images/points.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Title2():

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.image = pygame.image.load('images/title.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.center = self.screen_rect.center
        self.rect.top = self.screen_rect.top

    def blitme(self):
        self.screen.blit(self.image, self.rect)