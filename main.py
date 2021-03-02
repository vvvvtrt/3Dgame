import pygame
import sys
import settings
import raycaster
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

x = 6
y = 5
a = 0
while 1:
    c = raycaster.MainImage("map/level1.png")
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                a += 1
            elif i.key == pygame.K_RIGHT:
                a -= 1
            elif i.key == pygame.K_UP:
                x, y = c.step(cordinat=(x, y), a=a)
            elif i.key == pygame.K_DOWN:
                x, y = c.BackStep(cordinat=(x, y), a=a)

    if a >= 360:
        a = 0
    elif a < 0:
        a = 360 + a
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
