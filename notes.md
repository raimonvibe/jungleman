# Code step by step explaination

## Default setup (_you could automate that_)

First of all I create 3 files : `main.py`, `game.py` and `constants.py`. I copy and paste my code to get the monitor
resolution in constants.py.

## Creating the skeleton

I then go in game.py and start writing code. I create my init function. Then, I start the main function of the whole
game : `run`
There you can see the main loop which also has some default things that I copy and paste :

```python
def run(self):  # this is in game.py in the class Game
    clock = pygame.time.Clock()  # creating the clock that will help us force Frame rate
    while self.game_is_on:  # game loop
        clock.tick(FPS)  # Slows down the loop so it refreshes 60 times per second
        self.win.fill(BLACK)  # fill background
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if you push the red cross, it close the game
                self.game_is_on = False
```

I also pasted the default code you want to have in a clean project in `main.py`:

```python
if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Space Invader")
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    game = Game(win)
    game.run()
```

if you don't know why this s good go watch this video : [https://youtu.be/g_wlZ9IhbTs](https://youtu.be/g_wlZ9IhbTs)

## Diging into the game

### Spaceship object

Then I created the class Spaceship in the file `spaceship.py`, notice the upper case and lowercase, that is how you
usually want it to be.

Here is the basic init fonction :

```python
class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surface = img_spaceship  # sprite attribute
        self.rect = self.surface.get_rect()  # sprite attribute

        self.pos = vec(0, HEIGHT)
        self.vel = vec(0, 0)
```

vec stands for vector, it is a type that I discovered recently that is basically a tuple but better. it comes from the
line in `constants.py`

```python
vec = pygame.math.Vector2
```

basically it represents the x and y composant of position or velocity.

The two main fonctions are `move` and `update`. I think they are quite important to understand.

We now have this basic window where we can move the spaceship right and left
![img.png](img.png)

### Ennemies

```python
class Game:
    def __init__(self):
        # some stuff
        # instanciating objects
        self.spaceship = Spaceship()
        self.all_ennemies = pygame.sprite.Group()  # list of all ennemies
```

Here is what is most important in the init method of the Game class. Every ennemy that we will add to the game will be
added to the list/group all_ennemies You can consider it as a list, the fact that it is a sprite group isn't important.
_(it is used to detect collision between objects of a certain type)_

Let's create our class first

```python
class Ennemy(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()

        self.surface = img_ennemy  # instantiate image to display
        self.rect = self.surface.get_rect()  # instantiate position

        self.speed = 1
        self.pos = vec(x, 0)  # spawns on top somewhere on the x axis
        self.vel = (0, self.speed)
```

dont't worry too much about pygame.sprite.Sprite being an argument and super().__init__(), just remember that these two
are linked.

We then create the basic update fonction and we add a way to make an ennemy spawn every 3sec

We're good to go. Here is what it looks like for now :
![img_1.png](img_1.png)
The images are a bit small and the speed of the spaceship is way to slow, let's fix that by making those thing relative
to the screen size.

## Adjustments

First I scale the images that I hade already defined to an arbitrary size that depends on the screen:

```python
# sprites
blocksize = HEIGHT // 8  # arbitrary size that depends on the screen size

x, y = pygame.image.load("assets/s.png").get_size()
img_spaceship = pygame.transform.smoothscale(pygame.image.load("assets/s.png"), (blocksize, int(blocksize * y / x)))

x, y = pygame.image.load("assets/enemy.png").get_size()
img_ennemy = pygame.transform.smoothscale(pygame.image.load("assets/enemy.png"), (blocksize, int(blocksize * y / x)))
```

then I adjust de speed of the player :
if I want him to move at 10 block per second, I do this:

`            self.speed = 10 * blocksize // FPS
`

That is a very good way in my opinion to make the speed not change when you change device or FPS

## Death and end of game

Here is a basic check fonction to see wether the game is lost

```python

def check(self):
    """ we check for ennemies being arrived at the bottom"""
    for ennemy in self.all_ennemies:
        if ennemy.pos.y > HEIGHT - img_spaceship.get_size()[0]:
            self.lose()
        return False


def lose(self):
    self.game_is_on = False
```

Now when an ennemy arrives at the spaceship level, we close the window.

Let's make a way to kill those ennemies.

## Firing missiles

We create a basic missile class:

```python

class Missile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.surface = img_missile
        self.rect = self.surface.get_rect()

        self.speed = 5
        self.pos = vec(x, y - size_spaceship[0])
        self.vel = (0, self.speed)

    def update_pos(self):
        self.pos -= self.vel
        self.rect.midbottom = self.pos
```

We add a line in the Spaceship class to handle the option "fire"

```python

def move(self, info):
    if info == "right":
        self.vel = (self.speed, 0)
    elif info == "left":
        self.vel = (-self.speed, 0)
    elif info == "fire":
        if self.firing_state:
            self.fire()


def fire(self):
    self.fired_missiles.add(Missile(self.pos.x, self.pos.y))
```

Every time a new bullet is fired, we had A bullet/missile object to a group **instanciated in Spaceship**

`self.fired_missiles = pygame.sprite.Group()
`

### collision detection

In our Game file we had a fonction in our mainloop that will check if a missile is colliding with an ennemy. If so we
destroy both.

```python

def check_bullet_collision(self):
    for bullet in self.spaceship.fired_missiles:
        hits = pygame.sprite.spritecollide(bullet, self.all_ennemies, True)
        if hits:
            bullet.kill()
```

The argument `True` in the builtin `spritecollide` fonction removes any ennemy that collides with the bullet. Then we
remove the bullet if it hit something.

We add the code to make the firing available every 1 seconds

```python

if keys[pygame.K_SPACE] and time_elapsed_since_last_bullet_fired > 1000:
    time_elapsed_since_last_bullet_fired = 0
    self.spaceship.move("fire")
```

Every basic feature of the game is now ready ! You can now midify every parametre how you want, you can add music,
score, pause menu. You can also change the speed of your bullets or give a random speed to the ennemies when they spawn.

If you want to add a competitive dimension to the game you could make the ennemies spawn quicker with time. That would
be a good exercise !
