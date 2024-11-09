# Optimize this code
# Make the game look better

# Make the game more fun
# Make the game more challenging
# Make the game more interesting
# Make the game more enjoyable
# Make the game more addictive
# Make the game more appealing
# Make the game more engaging
# Make the game more exciting
# Make the game more thrilling
# Make the game more entertaining
# Make the game more appealing
# Make the game more interesting
# Make the game more exciting
# Make the game more thrilling
# Make the game more engaging


import pygame as pg  # Importing modules / setting constant variables and initializing
from sprites import *
from random import randint
from pygame import mixer
clock = pg.time.Clock()
pg.init()
pg.font.init()
pg.mixer.init()
pg.display.set_caption("Jungle-Man by raimoncoding")
# Set the size of the game window

info = pg.display.Info()
size = (info.current_w, info.current_h)
screen = pg.display.set_mode(size, pg.FULLSCREEN)
WIDTH, HEIGHT = 1400, 800

screen = pg.display.set_mode((WIDTH, HEIGHT))

FPS = 60
sprites = []  # Stores all the sprites
player = Player(200, 200)  # Makes a player
# hearts = Heart(50, 50)
# sprites.append(hearts)
sprites.append(player)
score = 0
game_win = 0
PINK = (255, 105, 180)
MINT = (192, 255, 238)
ORANGE = (255, 213, 128)
WINNER_FONT = pg.font.SysFont('comics', 100)
LOSER_FONT = pg.font.SysFont('comics', 100)

# BANANA_HIT_SOUND = pg.mixer.Sound('assets/monkeyhit2.mp3')
PLAYER_JUMP_SOUND = pg.mixer.Sound('assets/monkeythrow2.mp3')
BANANA_HIT_SOUND = pg.mixer.Sound('assets/monkeyhit2.mp3')
MONKEY_LAUGH_SOUND = pg.mixer.Sound('assets/monkeyLaugh.mp3')
MONKEY_LAUGH_SOUND2 = pg.mixer.Sound('assets/monkeyLaugh2.mp3')


# BANANA_HIT = pg.USEREVENT


pg.font.init()


def draw_window(win, player, platforms, fruits, hearts, score):  # Draws everything
    win.blit(pg.image.load("assets/sky.png"), (0, 0))
    win.blit(pg.image.load("assets/water.png"), (-50, 620))
    win.blit(pg.image.load("assets/water.png"), (100, 620))
    # win.blit(pg.image.load("assets/water.png"), (200, 620))
    win.blit(pg.image.load("assets/water.png"), (300, 620))
    # win.blit(pg.image.load("assets/water.png"), (400, 620))
    win.blit(pg.image.load("assets/water.png"), (500, 620))
    # win.blit(pg.image.load("assets/water.png"), (600, 620))
    win.blit(pg.image.load("assets/water.png"), (700, 620))
    # win.blit(pg.image.load("assets/water.png"), (800, 620))
    win.blit(pg.image.load("assets/water.png"), (900, 620))
    # win.blit(pg.image.load("assets/water.png"), (1000, 620))
    win.blit(pg.image.load("assets/water.png"), (1100, 620))
    # win.blit(pg.image.load("assets/water.png"), (1200, 620))
    win.blit(pg.image.load("assets/water.png"), (1250, 620))
    win.blit(pg.image.load("assets/cloud.png"), (0, 0))
    win.blit(pg.image.load("assets/cloud.png"), (110, 0))
    win.blit(pg.image.load("assets/tree2.png"), (0, 0))
    win.blit(pg.image.load("assets/mushroom2.png"), (0, 720))
    win.blit(pg.image.load("assets/cloud.png"), (210, 50))
    win.blit(pg.image.load("assets/cloud.png"), (410, 0))
    win.blit(pg.image.load("assets/cloud.png"), (240, 50))
    win.blit(pg.image.load("assets/cloud.png"), (410, 0))
    win.blit(pg.image.load("assets/cloud.png"), (510, 50))
    win.blit(pg.image.load("assets/cloud.png"), (410, 0))
    win.blit(pg.image.load("assets/mushroom2.png"), (640, 720))
    win.blit(pg.image.load("assets/mushroom1.png"), (600, 215))
    win.blit(pg.image.load("assets/cloud.png"), (640, 0))
    win.blit(pg.image.load("assets/cloud.png"), (710, 0))
    win.blit(pg.image.load("assets/cloud.png"), (810, 0))
    win.blit(pg.image.load("assets/cloud.png"), (910, 50))
    win.blit(pg.image.load("assets/cloud.png"), (960, 0))
    win.blit(pg.image.load("assets/cloud.png"), (1000, 50))
    win.blit(pg.image.load("assets/cloud.png"), (1050, 0))
    win.blit(pg.image.load("assets/tree1.png"), (1300, 610))
    win.blit(pg.image.load("assets/flower1.png"), (1300, 190))
    win.blit(pg.image.load("assets/flower2.png"), (950, 180))
    win.blit(pg.image.load("assets/bush.png"), (510, 275))

    for plat in platforms:
        plat.draw(win)
    # for water in waters:
    #     water.draw(win)
    for fruit in fruits:
        fruit.draw(win)
    for heart in hearts:
        heart.draw(win)
    # heart.draw(win)

    player.draw(win)
    screen.blit(pg.font.SysFont('comics', 60).render(
        f"Score: {score}", False, (192, 255, 238)), (100, 0))
    pg.display.update()


platforms = pg.sprite.Group()


# Makes a group for all platforms and fruits - this is like a list for sprites
fruits = pg.sprite.Group()
# Makes a group for all platforms and fruits - this is like a list for sprites
hearts = pg.sprite.Group()


sprites.append(Platform(0, 760, platforms))
sprites.append(Platform(170, 760, platforms))
sprites.append(Platform(340, 120, platforms))
sprites.append(Platform(80, 140, platforms))
# sprites.append(Heart(80, 90, hearts))
sprites.append(Platform(340, 660, platforms))
sprites.append(Platform(510, 310, platforms))
sprites.append(Platform(680, 260, platforms))
sprites.append(Platform(510, 610, platforms))
sprites.append(Platform(680, 560, platforms))
sprites.append(Platform(1020, 260, platforms))
sprites.append(Platform(1360, 260, platforms))
sprites.append(Platform(680, 760, platforms))
sprites.append(Platform(1000, 560, platforms))
sprites.append(Platform(850, 760, platforms))
sprites.append(Platform(1190, 760, platforms))
sprites.append(Platform(1360, 760, platforms))
sprites.append(Platform(1360, 450, platforms))


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, True, PINK)
    screen.blit(draw_text, (WIDTH/2 - draw_text.get_width() /
                            2, HEIGHT/2 - draw_text.get_height()/2))
    pg.display.update()
    pg.time.delay(5000)


def game_over(text):
    draw_text = WINNER_FONT.render(text, True, ORANGE)
    screen.blit(draw_text, (WIDTH/2 - draw_text.get_width() /
                            2, HEIGHT/2 - draw_text.get_height()/2))
    pg.display.update()
    pg.time.delay(5000)


heart_fallen = False
while True:  # Main game loop
    if randint(0, 40) == 0:
        # Makes fruit periodically
        sprites.append(Fruit(randint(150, 2400), 30, fruits))
    if randint(0, 40) == 0 and not heart_fallen:
        sprites.append(Heart(randint(50, 50), 30, hearts))  # Makes hearts
        heart_fallen = True

    clock.tick(FPS)  # Ticks clock

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            if event.type == pg.KEYDOWN:
                pg.key.set_repeat(50, 50)
                if event.key == pg.K_ESCAPE:
                    running = False
        if event.type == pg.KEYDOWN:  # Checks for keys down
            if event.key == pg.K_UP:
                player.jump()  # Jumps if up key is pressed
                PLAYER_JUMP_SOUND.play()

            if not player.jumping:
                if event.key == pg.K_LEFT:  # Left/right movement
                    player.vel.x -= 15
                if event.key == pg.K_RIGHT:
                    player.vel.x += 15
            elif player.jumping:
                if event.key == pg.K_LEFT:  # Left/right movement
                    player.vel.x -= 15
                if event.key == pg.K_RIGHT:
                    player.vel.x += 15
            else:

                if event.key == pg.K_LEFT:  # Left/right movement
                    player.vel.x -= 1
                if event.key == pg.K_RIGHT:
                    player.vel.x += 1
    #
    # # Check if player is going off the screen
    #
    # if player.x < 0:
    #     player.x = 0
    # if player.x + player.rect.width > size[0]:
    #     player.x = size[0] - player.rect.width
    # if player.y < 0:
    #     player.y = 0
    # if player.y + player.rect.height > size[1]:
    #     player.y = size[1] - player.rect.height
    # # check if player is in the water
    # if player.y + player.rect.height >= size[1]:
    #     # Game over
    #     MONKEY_LAUGH_SOUND2.play()
    #     game_over("You're in the water, Game Over!")
    #     break


    # Check if player is going off the screen
    if player.x < 0:
        player.x = 0
    elif player.x + player.rect.width > WIDTH:  # Gebruik WIDTH in plaats van size[0]
        player.x = WIDTH - player.rect.width

    if player.y < 0:
        player.y = 0
    elif player.y + player.rect.height > HEIGHT:  # Gebruik HEIGHT in plaats van size[1]
        player.y = HEIGHT - player.rect.height

    # check if player is in the water
    if player.y + player.rect.height >= HEIGHT:
        # Game over
        MONKEY_LAUGH_SOUND2.play()
        game_over("You're in the water, Game Over!")
        break


    if player.vel.y > 0:
        hits = pg.sprite.spritecollide(
            player, platforms, False)  # Collision with platform

        if hits:

            lowest = hits[0]
            for hit in hits:
                if hit.rect.bottom > lowest.rect.bottom:
                    lowest = hit
            if player.x < lowest.rect.right + 20 and \
                    player.x > lowest.rect.left - 20:
                if player.y < lowest.rect.centery:
                    player.y = lowest.rect.top + 1
                    player.vel.y = 0
                    player.jumping = False  # Landing on platform

    for heart in hearts:
        if heart.vel.y > 0:
            winning = pg.sprite.spritecollide(
                heart, platforms, False)  # Collision with platform

            if winning:

                lowest = winning[0]
                for winner in winning:
                    if winner.rect.bottom > lowest.rect.bottom:
                        lowest = winner
                if heart.x < lowest.rect.right + 20 and \
                        heart.x > lowest.rect.left - 20:
                    if heart.y < lowest.rect.centery:
                        heart.y = lowest.rect.top + 1
                        heart.vel.y = 0
                        heart.jumping = False  # Landing on platform

    winning = pg.sprite.spritecollide(
        player, hearts, True)  # Collision with player
    if winning:
        if not MONKEY_LAUGH_SOUND.get_num_channels() > 0:
            MONKEY_LAUGH_SOUND.play()
        game_win += (len(winning))  # Increases score

    winner_text = ""
    if game_win > 0:
        winner_text = "You have collected the heart!"

    if winner_text != "":
        draw_winner(winner_text)
        break

    for item in fruits:
        hits = pg.sprite.spritecollide(item, platforms, False)
        if hits:

            lowest = hits[0]
            for hit in hits:
                if hit.rect.bottom > lowest.rect.bottom:
                    lowest = hit
            if item.x < lowest.rect.right + 10 and \
                    item.x > lowest.rect.left - 10:
                if item.y < lowest.rect.centery:
                    item.y = lowest.rect.top + 1
                    item.vel.y = 0
                    if pg.sprite.collide_rect(item, lowest):
                        if item.y < lowest.rect.centery:
                            item.y = lowest.rect.top + 1
                            item.vel.y = 0
                            # if BANANA_HIT_SOUND.get_num_channels() == 0:
                            #     BANANA_HIT_SOUND.stop()
                            #     BANANA_HIT_SOUND.play(maxtime=500)

    # Player collision with fruits
    hits = pg.sprite.spritecollide(player, fruits, True)
    if hits:
        if BANANA_HIT_SOUND.get_num_channels() == 0:
            BANANA_HIT_SOUND.play(maxtime=500)
        score += (len(hits))  # Increases score

    player.update()
    # heart.update()
    for sprite in fruits:
        sprite.update()
    for sprite in hearts:
        sprite.update()
    for sprite in platforms:
        sprite.update()  # Updates all sprites

    draw_window(screen, player, platforms, fruits,
                hearts, score)  # Draws sprites

# Clean up
pg.quit()
