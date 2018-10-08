import pygame

class Settings():
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings."""
        #Screen Settings
        self.screen_width = 1000
        self.screen_height = 650
        self.bg_color = (30, 80, 200)

        #Screen Settings
        self.screen_width = 1000
        self.screen_height = 650
        self.bg_start_color = (0, 0, 0)

        #Bullet Settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 250, 0)
        self.bullets_allowed = 5

        #Alien Bullet Settings
        self.alien_bullet_speed = 3
        self.alien_bullet_width = 3
        self.alien_bullet_height = 10
        self.alien_bullet_color = (250,250,250)

        #How quickly the game speeds up
        self.speedup_scale = 1.2

        #How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        self.alien_speed_factor = 1.5
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        #Scoring
        self.alien_points = 10
        self.alien2_points = 20
        self.alien3_points = 40

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
