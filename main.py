import pygame
import sys
import settings
import raycaster
import keyboard
from threading import Thread, Event


class Keyboard(Thread):
    def __init__(self):
        Thread.__init__(self)
        global x
        global y
        self.stop = True

    def Stop(self):
        self.stop = False

    def run(self):
        keyboard.hook(control)
        while self.stop:
            pass


class Win(Thread):
    def __init__(self):
        Thread.__init__(self)
        global x
        global y
        self.stop = True

    def Stop(self):
        self.stop = False

    def run(self):
        g = raycaster.MainImage("map/level2.png")
        while self.stop:
            if g.pixel(x, y):
                print("You Win")


def control(key):
    global a
    global x
    global y
    if key.event_type != "up":
        if key.name == "up":
            c = raycaster.MainImage("map/level2.png")
            x, y = c.step(cordinat=(x, y), a=a)

        elif key.name == "right":
            a -= 1

        elif key.name == "left":
            a += 1


def image(screen, img, x, y, r):
    image = pygame.image.load(img).convert_alpha()
    image = pygame.transform.scale(
        image, (r, 30))
    screen.blit(image, (x, y))


FPS = settings.FPS
WIN_WIDTH = settings.Width
WIN_HEIGHT = settings.Height
WHITE = (255, 255, 255)

clock = pygame.time.Clock()
sc = pygame.display.set_mode(
    (WIN_WIDTH, WIN_HEIGHT))

g = Keyboard()
g.start()

x = 5
y = 5
a = 0
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            g.Stop()
            sys.exit()

    sc.fill(WHITE)

    c = raycaster.MainImage("map/level2.png")
    c = c.raycasting(cordinat=(x, y), a=a)
    textur = []
    for i in range(30):
        if c[i][0] != (255, 255, 255):
            pygame.draw.rect(sc, c[i][0],
                             (30 * i, 145 + c[i][3], 30, 255 - c[i][3]))
            if c[i][0] == (0, 0, 0):
                image(sc, "textur/stoun.jpg", 145 + c[i][3], 30 * i, 255 - c[i][3])
            elif c[i][0] == (255, 201, 14):
                image(sc, "textur/brick.jpg", 145 + c[i][3], 30 * i, 255 - c[i][3])
            elif c[i][0] == (63, 72, 204):
                image(sc, "textur/bithon.jpg", 145 + c[i][3], 30 * i, 255 - c[i][3])
        else:
            pygame.draw.rect(sc, c[i][0],
                             (30 * i, 145, 30, 255))
    pygame.display.update()
    if a >= 360:
        a = 0
    elif a < 0:
        a = 360 + a
    clock.tick(FPS)
