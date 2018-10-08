import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from button import Button2
from ship import Ship
from title import Title
from title import Title2
from bunker import Bunker

import game_functions as gf

def run_game():
    #Initialize pygame, settings, and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    pygame.mixer.music.load('sounds/background.mp3')
    pygame.mixer.music.play(-1)

    #Make the play button
    play_button = Button(ai_settings, screen, "Play Game")
    hs_button = Button2(ai_settings, screen, "High Scores")
    title = Title(ai_settings, screen)
    title2 = Title2(ai_settings, screen)

    #Create an instance to store game stats and create a scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    #Make a ship, a group of bullets, a group of bunkers, and a group of aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    abullets = Group()
    aliens = Group()
    bunkers = Group()

    #Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #Create the bunkers
    gf.create_bunker_rows(ai_settings, screen, bunkers)

    #Start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, hs_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets, bunkers)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button, hs_button, title, title2, bunkers)

run_game()
