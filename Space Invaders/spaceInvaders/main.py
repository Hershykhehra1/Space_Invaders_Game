import pygame, random
import sys
from game import Game


pygame.init()

SCREEN_WIDTH = 750
SCREEN_HEIGHT = 700
OFFSET = 50

screen = pygame.display.set_mode((SCREEN_WIDTH + OFFSET, SCREEN_HEIGHT + 2 * OFFSET))

pygame.display.set_caption("Space Invaders")
yellow = (243, 216, 63)

font = pygame.font.Font("Font/monogram.ttf", 40)
game_over_surface = font.render("Game Over", False, yellow)
score_text_surface = font.render("Score", False, yellow)
highscore_text_surface = font.render("High Score", False, yellow)


clock = pygame.time.Clock()
grey = (128, 128, 128)

game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, OFFSET)

# Events
SHOOT_LASER = pygame.USEREVENT
pygame.time.set_timer(SHOOT_LASER, 300)

mystery_ship = pygame.USEREVENT + 1
pygame.time.set_timer(mystery_ship, random.randint(4000,8000))


while True:

    for event in pygame.event.get():
        # check if there is a QUIT event
        if event.type == pygame.QUIT:
            # break out
            pygame.quit()
            # close program
            sys.exit()

        if event.type == SHOOT_LASER and game.run:
            game.alien_shoot_laser()

        if event.type == mystery_ship and game.run:
            game.create_mystery_ship()
            pygame.time.set_timer(mystery_ship, random.randint(4000,8000))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and game.run == False:
            game.reset()



    if game.run:
        game.spaceship_group.update()
        game.move_aliens()
        game.alien_lasers_group.update()
        game.mystery_ship_group.update()
        game.check_for_collisions()

    screen.fill(grey)

    pygame.draw.rect(screen, yellow, (10, 10, 780, 780), 2, 0, 60, 60, 60, 60, )
    pygame.draw.line(screen, yellow, (25, 730,), (775, 730), 30)

    if not game.run:
        screen.blit(game_over_surface, (570, 740, 50, 50))

    x = 50
    for life in range(game.lives):
        screen.blit(game.spaceship_group.sprite.image, (x, 745))
        x += 50



    screen.blit(score_text_surface, (50, 15, 50, 50))
    formatted_score = str(game.score).zfill(5)
    score_surface = font.render(formatted_score, False, yellow)
    screen.blit(score_surface, (50, 40, 50, 50))

    screen.blit(highscore_text_surface, (550, 15, 50, 50))
    formatted_highscore = str(game.highscore).zfill(5)
    highscore_surface = font.render(formatted_highscore, False, yellow)
    screen.blit(highscore_surface, (625, 40, 50, 50))



    game.spaceship_group.draw(screen)
    game.spaceship_group.sprite.lasers_group.draw(screen)

    for obstacle in game.obstacles:
        obstacle.blocks_group.draw(screen)

    game.aliens_group.draw(screen)
    game.alien_lasers_group.draw(screen)
    game.mystery_ship_group.draw(screen)

    pygame.display.update()
    # set fps (while loop runs 60 times per second)
    clock.tick(60)
