import pygame
import sys
import settings
import raycaster
from time import sleep
from threading import Thread


class Win(Thread):
    def __init__(self):
        Thread.__init__(self)
        global x
        global y
        self.stop = True

    def Stop(self):
        self.stop = False

    def run(self):
        g = raycaster.MainImage("map/level1.png")
        while self.stop:
            if g.pixel(x, y):
                print("You Win")


class Traffic(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        global x
        global y
        global a
        global right
        global left
        global ForwardStep
        global BackStep
        global stop
        c = raycaster.MainImage("map/level1.png")
        while not stop:
            if ForwardStep:
                x, y = c.step(cordinat=(x, y), a=a)
            elif BackStep:
                x, y = c.BackStep(cordinat=(x, y), a=a)
            if right:
                a -= 1
            elif left:
                a += 1
            sleep(0.1)

def angle():
    global a
    if a >= 360:
        a = 0
    elif a < 0:
        a = 360 + a


def image(screen, img, x, y, r):
    image = pygame.image.load(img).convert_alpha()
    image = pygame.transform.scale(
        image, (30, r))
    screen.blit(image, (x, y))


FPS = settings.FPS
WIN_WIDTH = settings.Width
WIN_HEIGHT = settings.Height
WHITE = (255, 255, 255)

clock = pygame.time.Clock()
sc = pygame.display.set_mode(
    (WIN_WIDTH, WIN_HEIGHT))

playWin = Win()
playWin.start()

control = Traffic()
control.start()

right = False
left = False
ForwardStep = False
BackStep = False
stop = False

x = 6
y = 5
a = 0

while True:
    c = raycaster.MainImage("map/level1.png")
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            stop = True
            playWin.Stop()
            sys.exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                left = True
            elif i.key == pygame.K_RIGHT:
                right = True
            elif i.key == pygame.K_UP:
                ForwardStep = True
            elif i.key == pygame.K_DOWN:
                BackStep = True
        elif i.type == pygame.KEYUP:
            if i.key == pygame.K_LEFT:
                left = False
            if i.key == pygame.K_RIGHT:
                right = False
            if i.key == pygame.K_UP:
                ForwardStep = False
            if i.key == pygame.K_DOWN:
                ForwardStep = False
    angle()
    sc.fill(WHITE)
    c = c.raycasting(cordinat=(x, y), a=a)
    textur = []
    for i in range(30):
        if c[i][0] != (255, 255, 255):
            if c[i][0] == (0, 0, 0, 255):
                image(sc, "textur/stoun.jpg", 30 * i, 145 + c[i][3], 255 - c[i][3])
            elif c[i][0] == (255, 201, 14, 255):
                image(sc, "textur/brick.jpg", 30 * i, 145 + c[i][3], 255 - c[i][3])
            elif c[i][0] == (63, 72, 204, 255):
                image(sc, "textur/bithon.jpg", 30 * i, 145 + c[i][3], 255 - c[i][3])
            else:
                pygame.draw.rect(sc, c[i][0],
                                 (30 * i, 145 + c[i][3], 30, 255 - c[i][3]))
        else:
            pygame.draw.rect(sc, c[i][0],
                             (30 * i, 145, 30, 255))
    pygame.display.update()
    clock.tick(FPS)
