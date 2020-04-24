import pygame
import random
import pygame.freetype
from ai import Logic


class snake(object):
    """snake class"""

    def __init__(self, x, y):
        super(snake, self).__init__()
        self.length = 9
        self.size = 9
        self.dire = 0
        self.x = x
        self.y = y
        self.prevx = 0
        self.prevy = 0
        self.movement = None
        self.point = 0
        self.direction = None
        self.game = 1
        self.pressed = None
        self.ai = 0
        self.comp = 'OFF'

    def keys(self):
        self.pressed = pygame.key.get_pressed()
        return self.pressed

    def movedir(self):
        self.keys()
        if self.game:
            if (self.pressed[pygame.K_UP] and self.movement is not 1) or self.ai == 1:
                self.movement = 0
                self.dire = 1
            if (self.pressed[pygame.K_DOWN] and self.movement is not 0) or self.ai == 2:
                self.movement = 1
                self.dire = 1
            if (self.pressed[pygame.K_LEFT] and self.movement is not 3) or self.ai == 3:
                self.movement = 2
                self.dire = 1
            if (self.pressed[pygame.K_RIGHT] and self.movement is not 2) or self.ai == 4:
                self.movement = 3
                self.dire = 1

    def move(self):
        self.movedir()
        if self.dire and (self.movement == 0):
            self.prevy = self.y
            self.prevx = self.x
            self.y -= self.size
        if self.dire and (self.movement == 1):
            self.prevy = self.y
            self.prevx = self.x
            self.y += self.size
        if self.dire and (self.movement == 2):
            self.prevy = self.y
            self.prevx = self.x
            self.x -= self.size
        if self.dire and (self.movement == 3):
            self.prevy = self.y
            self.prevx = self.x
            self.x += self.size

    def restart(self, lilsnake, snakes, food):
        self.keys()
        if self.pressed[pygame.K_SPACE] and not self.game:
            snakes = [lilsnake]
            food.alive = 0
            self.x = width / 2
            self.y = height / 2
            self.game = 1
            self.point = 0
        return snakes


class food(object):
    """food for our lil snake"""

    def __init__(self):
        super(food, self).__init__()
        self.x = 9 * random.randint(1, 48)
        self.y = 9 * random.randint(1, 48)
        self.alive = 0
        self.size = 9
        self.colorrange = [(0, 0, 255), (0, 255, 0),
                           (255, 0, 0), (0, 255, 255)]
        self.color = self.colorrange[random.randint(0, 3)]
        self.prevcolor = None

    def produce(self):
        pygame.draw.rect(
            win, self.color, (self.x, self.y, self.size, self.size))

    def newFood(self):
        if not self.alive:
            self.x = 9 * random.randint(1, 48)
            self.y = 9 * random.randint(1, 48)
        self.alive = 1
        self.prevcolor = self.color
        self.color = self.colorrange[random.randint(0, 3)]


class recti(object):
    """docstring for recti"""

    def __init__(self, x, y):
        super(recti, self).__init__()
        self.x = x
        self.y = y
        self.prevy = 0
        self.prevy = 0
        self.size = 9


def bound(height, width):
    restart = 0
    if lilsnake.y < 9:
        lilsnake.direction = 1
        lilsnake.y = 9
        lilsnake.movement = 9
        restart = 1
    if lilsnake.y > height - lilsnake.size:
        lilsnake.direction = 1
        lilsnake.y = height - lilsnake.size - 9
        lilsnake.movement = 9
        restart = 1
    if lilsnake.x < 9:
        lilsnake.direction = 2
        lilsnake.x = 9
        lilsnake.movement = 9
        restart = 1
    if lilsnake.x > width - lilsnake.size:
        lilsnake.direction = 2
        lilsnake.x = width - lilsnake.size - 9
        lilsnake.movement = 9
        restart = 1
    return restart


pygame.init()
width = 450
height = 450


def text_dis(text, pos):
    text_surface, rect = GAME_FONT.render(text, (255, 255, 255))
    win.blit(text_surface, pos)


canvas = width, height
clock = pygame.time.Clock()
win = pygame.display.set_mode(canvas)
pygame.display.set_caption('Little Sneaky Snake')
GAME_FONT = pygame.freetype.SysFont('freesansbold.ttf', 24)
lilsnake = snake(width / 2, height / 2)
snakes = []
snakes.append(lilsnake)
food = food()
AI = Logic()
lilsnake.comp = 'ON'


def boundary():
    color = (0, 230, 0)
    pygame.draw.rect(win, color, (0, 0, width, lilsnake.size))
    pygame.draw.rect(
        win, color, (0, height - lilsnake.size, width, lilsnake.size))
    pygame.draw.rect(win, color, (0, 0, lilsnake.size, height))
    pygame.draw.rect(
        win, color, (width - lilsnake.size, 0, lilsnake.size, height))


def col(s, food):
    if (lilsnake.x == food.x) and (lilsnake.y == food.y):
        lilsnake.point += 1
        food.alive = 0
        if (lilsnake.movement == 0):
            snakes.append(recti(s.x, s.y + 9 * lilsnake.point))
        elif (lilsnake.movement == 1):
            snakes.append(recti(s.x, s.y - 9 * lilsnake.point))
        elif lilsnake.movement == 2:
            snakes.append(recti(s.x + 9 * lilsnake.point, s.y))
        else:
            snakes.append(recti(s.x - 9 * lilsnake.point, s.y))


n = 0
run = True
while run:
    clock.tick(15)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 255, 255), (lilsnake.x,
                                            lilsnake.y, lilsnake.size, lilsnake.size))
    for n, s in enumerate(snakes):
        if n > 0:
            if lilsnake.movement is 9:
                pygame.draw.rect(win, food.prevcolor,
                                 (s.x, s.y, lilsnake.size, lilsnake.size))

            else:
                snakes[n].prevx = snakes[n].x
                snakes[n].prevy = snakes[n].y
                snakes[n].x = snakes[n - 1].prevx
                snakes[n].y = snakes[n - 1].prevy
                pygame.draw.rect(win, food.prevcolor,
                                 (s.x, s.y, lilsnake.size, lilsnake.size))

    lilsnake.move()
    if lilsnake.comp == 'ON':
        lilsnake.ai = AI.label(lilsnake.x, lilsnake.y,
                               food.x, food.y, lilsnake.movement)

    if not lilsnake.game:
        text_dis('You Lost, Press Space to Continue',
                 (width / 2 - 200, height / 2 - 25))
        snakes = lilsnake.restart(lilsnake, snakes, food)
    if bound(height, width):
        n += 0
        lilsnake.game = 0
        if n < 4:
            win.fill((80, 80, 80))

    if food.alive:
        food.produce()
    else:
        food.newFood()

    col(lilsnake, food)
    text_dis(str(lilsnake.point), (400, 400))
    boundary()
    pygame.display.update()

pygame.quit()
quit()
