import pygame as pg
from sprites import *
from random import randint
from pygame import mixer

# Initialisatie
clock = pg.time.Clock()
pg.init()
pg.font.init()
pg.mixer.init()
pg.display.set_caption("Jungle-Man by raimoncoding")

# Scherm setup met scaling
info = pg.display.Info()
SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h

# Bereken schaalfactoren
BASE_WIDTH = 1400
BASE_HEIGHT = 800
SCALE_X = SCREEN_WIDTH / BASE_WIDTH
SCALE_Y = SCREEN_HEIGHT / BASE_HEIGHT

# Scherm instellen
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pg.FULLSCREEN)
WIDTH, HEIGHT = SCREEN_WIDTH, SCREEN_HEIGHT

# Game constanten
FPS = 60
PINK = (255,105,180)
MINT = (192,255,238)
ORANGE = (255, 213, 128)

# Font scaling
FONT_SIZE = int(100 * SCALE_Y)
WINNER_FONT = pg.font.SysFont('comics', FONT_SIZE)
LOSER_FONT = pg.font.SysFont('comics', FONT_SIZE)

# Geluiden
PLAYER_JUMP_SOUND = pg.mixer.Sound('assets/monkeythrow2.mp3')
BANANA_HIT_SOUND = pg.mixer.Sound('assets/monkeyhit2.mp3')
MONKEY_LAUGH_SOUND = pg.mixer.Sound('assets/monkeyLaugh.mp3')
MONKEY_LAUGH_SOUND2 = pg.mixer.Sound('assets/monkeyLaugh2.mp3')

# Sprite groepen initialisatie
sprites = []
platforms = pg.sprite.Group()
fruits = pg.sprite.Group()
hearts = pg.sprite.Group()

# Speler maken met geschaalde positie
player = Player(int(200 * SCALE_X), int(200 * SCALE_Y))
sprites.append(player)

# Score initialisatie
score = 0
game_win = 0

def scale_pos(x, y):
    return (int(x * SCALE_X), int(y * SCALE_Y))

# Alle achtergrond elementen met originele coördinaten
background_elements = [
    ("assets/sky.png", (0, 0)),
    ("assets/water.png", (-50, 620)),
    ("assets/water.png", (100, 620)),
    ("assets/water.png", (300, 620)),
    ("assets/water.png", (500, 620)),
    ("assets/water.png", (700, 620)),
    ("assets/water.png", (900, 620)),
    ("assets/water.png", (1100, 620)),
    ("assets/water.png", (1250, 620)),
    ("assets/cloud.png", (0, 0)),
    ("assets/cloud.png", (110, 0)),
    ("assets/tree2.png", (0, 0)),
    ("assets/mushroom2.png", (0, 720)),
    ("assets/cloud.png", (210, 50)),
    ("assets/cloud.png", (410, 0)),
    ("assets/cloud.png", (240, 50)),
    ("assets/cloud.png", (410, 0)),
    ("assets/cloud.png", (510, 50)),
    ("assets/cloud.png", (410, 0)),
    ("assets/mushroom2.png", (640, 720)),
    ("assets/mushroom1.png", (600, 215)),
    ("assets/cloud.png", (640, 0)),
    ("assets/cloud.png", (710, 0)),
    ("assets/cloud.png", (810, 0)),
    ("assets/cloud.png", (910, 50)),
    ("assets/cloud.png", (960, 0)),
    ("assets/cloud.png", (1000, 50)),
    ("assets/cloud.png", (1050, 0)),
    ("assets/tree1.png", (1300, 610)),
    ("assets/flower1.png", (1300, 190)),
    ("assets/flower2.png", (950, 180)),
    ("assets/bush.png", (510, 275))
]

def draw_window(win, player, platforms, fruits, hearts, score):
    # Teken alle achtergrond elementen met scaling
    for image_path, (x, y) in background_elements:
        image = pg.image.load(image_path)
        scaled_image = pg.transform.scale(image, 
            (int(image.get_width() * SCALE_X), 
             int(image.get_height() * SCALE_Y)))
        win.blit(scaled_image, scale_pos(x, y))

    # Teken alle game elementen
    for plat in platforms:
        plat.draw(win)
    for fruit in fruits:
        fruit.draw(win)
    for heart in hearts:
        heart.draw(win)
    player.draw(win)
    
    # Teken score
    score_font = pg.font.SysFont('comics', int(60 * SCALE_Y))
    score_text = score_font.render(f"Score: {score}", False, MINT)
    screen.blit(score_text, scale_pos(100, 0))
    
    pg.display.update()

    # Platform posities
platform_positions = [
    (0, 760),
    (170, 760),
    (340, 120),
    (80, 140),
    (340, 660),
    (510, 310),
    (680, 260),
    (510, 610),
    (680, 560),
    (1020, 260),
    (1360, 260),
    (680, 760),
    (1000, 560),
    (850, 760),
    (1190, 760),
    (1360, 760),
    (1360, 450)
]

# Maak alle platforms met geschaalde posities
for pos_x, pos_y in platform_positions:
    sprites.append(Platform(int(pos_x * SCALE_X), int(pos_y * SCALE_Y), platforms))

def draw_winner(text):
    draw_text = WINNER_FONT.render(text, True, PINK)
    screen.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, 
                           HEIGHT/2 - draw_text.get_height()/2))
    pg.display.update()
    pg.time.delay(5000)

def game_over(text):
    draw_text = WINNER_FONT.render(text, True, ORANGE)
    screen.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, 
                           HEIGHT/2 - draw_text.get_height()/2))
    pg.display.update()
    pg.time.delay(5000)

# Game loop
heart_fallen = False
running = True
while running:
    if randint(0, 40) == 0:
        sprites.append(Fruit(int(randint(150, int(2400 * SCALE_X))), 
                           int(30 * SCALE_Y), fruits))
    if randint(0, 40) == 0 and not heart_fallen:
        sprites.append(Heart(int(50 * SCALE_X), int(30 * SCALE_Y), hearts))
        heart_fallen = True

    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            pg.key.set_repeat(50, 50)
            if event.key == pg.K_ESCAPE:
                running = False
            if event.key == pg.K_UP:
                player.jump()
                PLAYER_JUMP_SOUND.play()
            if not player.jumping:
                if event.key == pg.K_LEFT:
                    player.vel.x -= int(15 * SCALE_X)
                if event.key == pg.K_RIGHT:
                    player.vel.x += int(15 * SCALE_X)
            elif player.jumping:
                if event.key == pg.K_LEFT:
                    player.vel.x -= int(15 * SCALE_X)
                if event.key == pg.K_RIGHT:
                    player.vel.x += int(15 * SCALE_X)
            else:
                if event.key == pg.K_LEFT:
                    player.vel.x -= int(1 * SCALE_X)
                if event.key == pg.K_RIGHT:
                    player.vel.x += int(1 * SCALE_X)

    # Scherm grenzen check
    if player.x < 0:
        player.x = 0
    elif player.x + player.rect.width > WIDTH:
        player.x = WIDTH - player.rect.width

    if player.y < 0:
        player.y = 0
    elif player.y + player.rect.height > HEIGHT:
        player.y = HEIGHT - player.rect.height
        MONKEY_LAUGH_SOUND2.play()
        game_over("You're in the water, Game Over!")
        break

    # Platform collisions
    if player.vel.y > 0:
        hits = pg.sprite.spritecollide(player, platforms, False)
        if hits:
            lowest = hits[0]
            for hit in hits:
                if hit.rect.bottom > lowest.rect.bottom:
                    lowest = hit
            platform_margin = int(20 * SCALE_X)
            if (player.x < lowest.rect.right + platform_margin and 
                player.x > lowest.rect.left - platform_margin):
                if player.y < lowest.rect.centery:
                    player.y = lowest.rect.top
                    player.vel.y = 0
                    player.jumping = False

    # Heart collisions
    for heart in hearts:
        if heart.vel.y > 0:
            winning = pg.sprite.spritecollide(heart, platforms, False)
            if winning:
                lowest = winning[0]
                for winner in winning:
                    if winner.rect.bottom > lowest.rect.bottom:
                        lowest = winner
                heart_margin = int(20 * SCALE_X)
                if (heart.x < lowest.rect.right + heart_margin and 
                    heart.x > lowest.rect.left - heart_margin):
                    if heart.y < lowest.rect.centery:
                        heart.y = lowest.rect.top
                        heart.vel.y = 0
                        heart.jumping = False

    # Heart collection
    winning = pg.sprite.spritecollide(player, hearts, True)
    if winning:
        if not MONKEY_LAUGH_SOUND.get_num_channels() > 0:
            MONKEY_LAUGH_SOUND.play()
        game_win += len(winning)

    winner_text = ""
    if game_win > 0:
        winner_text = "You have collected the heart!"

    if winner_text != "":
        draw_winner(winner_text)
        break

    # Fruit collisions
    for item in fruits:
        hits = pg.sprite.spritecollide(item, platforms, False)
        if hits:
            lowest = hits[0]
            for hit in hits:
                if hit.rect.bottom > lowest.rect.bottom:
                    lowest = hit
            fruit_margin = int(10 * SCALE_X)
            if (item.x < lowest.rect.right + fruit_margin and 
                item.x > lowest.rect.left - fruit_margin):
                if item.y < lowest.rect.centery:
                    item.y = lowest.rect.top
                    item.vel.y = 0

    # Fruit collection
    hits = pg.sprite.spritecollide(player, fruits, True)
    if hits:
        if BANANA_HIT_SOUND.get_num_channels() == 0:
            BANANA_HIT_SOUND.play(maxtime=500)
        score += len(hits)

    # Update alle sprites
    player.update()
    for sprite in fruits:
        sprite.update()
    for sprite in hearts:
        sprite.update()
    for sprite in platforms:
        sprite.update()

    # Teken alles
    draw_window(screen, player, platforms, fruits, hearts, score)

# Clean up
pg.quit()
