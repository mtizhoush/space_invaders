import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien
from alien import Alien2
from alien import Alien3
from bunker import Bunker

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen,ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet"""
    #Create a new bullet and add it to the bullets group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
        pygame.mixer.Sound.play(new_bullet.bullet_sound)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, stats, sb, play_button, hs_button, ship, aliens, bullets):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, hs_button, ship, aliens, bullets, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, sb, play_button, hs_button, ship, aliens, bullets, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    hs_button_clicked = hs_button.rect.collidepoint(mouse_x, mouse_y)

    if button_clicked and not stats.game_active:
        #Reset the game settings
        ai_settings.initialize_dynamic_settings()

        #Hide the mouse cursor
        pygame.mouse.set_visible(False)

        #Reset the game stats
        stats.reset_stats()
        stats.game_active = True

        #Reset the scoreboard images
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        #Empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        #Create a new fleet and center the ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

    elif hs_button_clicked and not stats.game_active:
        sb.prep_high_score()

def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button, hs_button, title, title2, bunkers):
    """Update images on the screen and flip to the new screen"""
    #Redraw the scren during each pass through the loop
    screen.fill(ai_settings.bg_color)

    #Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    bunkers.draw(screen)

    #Draw the score info
    sb.show_score()

    #Draw the play button if the game is inactive
    if not stats.game_active:
        screen.fill(ai_settings.bg_start_color)
        title.blitme()
        title2.blitme()
        play_button.draw_button()
        hs_button.draw_button()

    #Make the most recently drawn screen visible
    pygame.display.flip()

def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets, bunkers):
    #Update bullet positions
    bullets.update()

    #Get rid of bullest that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets, bunkers)

def get_number_aliens_x(ai_settings, alien_width):
    """Determine the number of aliens that fit in a row"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width)) - 2
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def get_number_bunker_x(ai_settings, bunker_width):
    """Determine the number of aliens that fit in a row"""
    available_space_x = ai_settings.screen_width - 2 * bunker_width
    number_bunkers_x = int(available_space_x / (2 * bunker_width)) - 2
    return number_bunkers_x

def create_bunker(ai_settings, screen, bunkers, bunker_number):
    bunker = Bunker(ai_settings, screen)
    bunker_width = bunker.rect.width + 20
    bunker.x = bunker_width + 2.4 * bunker_width * bunker_number
    bunker.y = 500
    bunker.rect.x = bunker.x
    bunker.rect.y = bunker.y
    bunkers.add(bunker)

def create_bunker_rows(ai_settings, screen, bunkers):
    bunker = Bunker(ai_settings, screen)

    number_bunkers_x = get_number_aliens_x(ai_settings, bunker.rect.width)
    number_rows = 1

    for row_number in range(number_rows):
        for bunker_number in range(number_bunkers_x):
            create_bunker(ai_settings, screen, bunkers, bunker_number)

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create an alien and place it in the row"""
    alien = Alien(ai_settings, screen, 1)
    alien_width = alien.rect.width + 14
    alien.x = alien_width + 1.1 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 1.5 * alien.rect.height * row_number
    alien.type = 1
    aliens.add(alien)

def create_alien2(ai_settings, screen, aliens, alien_number, row_number):
    alien2 = Alien2(ai_settings, screen, 2)
    alien2_width = alien2.rect.width + 2
    alien2.x = alien2_width + 1.2 * alien2_width * alien_number
    alien2.rect.x = alien2.x
    alien2.rect.y = alien2.rect.height + 1 * alien2.rect.height * row_number
    alien2.type = 2
    aliens.add(alien2)

def create_alien3(ai_settings, screen, aliens, alien_number, row_number):
    alien3 = Alien3(ai_settings, screen, 3)
    alien3_width = alien3.rect.width
    alien3.x = alien3_width + 1.2 * alien3_width * alien_number
    alien3.rect.x = alien3.x
    alien3.rect.y = alien3.rect.height + 0.9 * alien3.rect.height * row_number
    alien3.type = 3
    aliens.add(alien3)

def create_fleet(ai_settings, screen, ship, aliens):
    """Create a full fleet of aliens"""
    #Create an alien and find the number of aliens in a row
    alien = Alien(ai_settings, screen, 3)

    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    #Create the fleet of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            if row_number in range(2):
                create_alien(ai_settings, screen, aliens, alien_number, row_number)
            elif row_number in range(4):
                create_alien2(ai_settings, screen, aliens, alien_number, row_number)
            elif row_number in range(6):
                create_alien3(ai_settings, screen, aliens, alien_number, row_number)

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets, bunkers):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            for alien in aliens:
                if alien.type == 1:
                     stats.score += ai_settings.alien_points * len(aliens)
                elif alien.type == 2:
                    stats.score += ai_settings.alien2_points * len(aliens)
                elif alien.type == 3:
                    stats.score += ai_settings.alien3_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        # If the entire fleet is destroyed, start a new level
        bullets.empty()
        ai_settings.increase_speed()

        # Increase level
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)

def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets):
    if stats.ships_left > 0:
        #Decrement ships left
        stats.ships_left -= 1

        #Update scoreboard
        sb.prep_ships()

        #Empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        #Create a new fleet and center the ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        #Pause
        pygame.mixer.music.stop()
        sleep(0.5)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)
            break

def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

def update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    #Look for alien-ship collisions
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)

    #Look for aliens hitting the botton of screen
    check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets)
