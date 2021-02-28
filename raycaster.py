from PIL import Image
import settings
import math


class MainImage:
    def __init__(self, map):
        super().__init__()
        self.map = Image.open(map)
        self.pixels = self.map.load()
        self.x, self.y = self.map.size

    def raycasting(self, cordinat=(1, 1), a=90):
        # y = kx + b && k = tgA
        x, y = cordinat
        ArrayPoints = []
        masg = []
        for i in range(a + (settings.Overview // 2), a - (settings.Overview // 2) - 1, -1):
            if i < 0:
                masg.append(360 + i)
            elif i > 360:
                masg.append((i - 360))
            else:
                masg.append(i)

        # range(a + (settings.Overview // 2), a - (settings.Overview // 2) - 1, -1):
        for i in masg:
            k = math.tan(math.radians(i))
            b = y - k * x
            if i not in (0, 90, 180, 270, 360):
                if 270 > i > 90:
                    for j in range(1, 400):
                        x1 = x - j
                        y1 = k * x1 + b
                        if 0 <= x1 < self.x and 0 <= y1 < self.y:
                            c = self.pixels[int(x1), int(y1)]
                            if c != (255, 255, 255, 255) and c != (254, 254, 254, 255) and c != (
                                    255, 255, 255) and c != (254, 254, 254):
                                ArrayPoints.append([c, x1, y1, j])
                                break
                    else:
                        ArrayPoints.append([(255, 255, 255), 0, 0, j])
                else:
                    for j in range(1, 400):
                        x1 = x + j
                        y1 = k * x1 + b
                        if 0 <= x1 < self.x and 0 <= y1 < self.y:
                            c = self.pixels[int(x1), int(y1)]
                            if c != (255, 255, 255, 255) and c != (254, 254, 254, 255) and c != (
                                    255, 255, 255) and c != (254, 254, 254):
                                ArrayPoints.append([c, x1, y1, j])
                                break
                    else:
                        ArrayPoints.append([(255, 255, 255), 0, 0, j])
            else:
                if i == 0 or i == 360:
                    for j in range(1, 400):
                        x1 = x + j
                        y1 = 0 + y
                        if 0 <= x1 < self.x and 0 <= y1 < self.y:
                            c = self.pixels[int(x1), int(y1)]
                            if c != (255, 255, 255, 255) and c != (254, 254, 254, 255) and c != (
                                    255, 255, 255) and c != (254, 254, 254):
                                ArrayPoints.append([c, x1, y1, j])
                                break
                elif i == 180:
                    for j in range(1, 400):
                        x1 = x - j
                        y1 = 0 + y
                        if 0 <= x1 < self.x and 0 <= y1 < self.y:
                            c = self.pixels[int(x1), int(y1)]
                            if c != (255, 255, 255, 255) and c != (254, 254, 254, 255) and c != (
                                    255, 255, 255) and c != (254, 254, 254):
                                ArrayPoints.append([c, x1, y1, j])
                                break
                if i == 90:
                    for j in range(1, 400):
                        x1 = 0 + x
                        y1 = y - j
                        if 0 <= x1 < self.x and 0 <= y1 < self.y:
                            c = self.pixels[int(x1), int(y1)]
                            if c != (255, 255, 255, 255) and c != (254, 254, 254, 255) and c != (
                                    255, 255, 255) and c != (254, 254, 254):
                                ArrayPoints.append([c, x1, y1, j])
                                break
                elif i == 270:
                    for j in range(1, 400):
                        x1 = 0 + x
                        y1 = y + j
                        if 0 <= x1 < self.x and 0 <= y1 < self.y:
                            c = self.pixels[int(x1), int(y1)]
                            if c != (255, 255, 255, 255) and c != (254, 254, 254, 255) and c != (
                                    255, 255, 255) and c != (254, 254, 254):
                                ArrayPoints.append([c, x1, y1, j])
                                break
        return ArrayPoints

    def step(self, cordinat=(0, 0), a=0):
        x, y = cordinat
        ArrayPoints = []
        masg = []
        k = math.tan(math.radians(a))
        b = y - k * x
        if a not in (0, 90, 180, 270, 360):
            if 270 > a > 90:
                x1 = x - 1
                y1 = int(k * x1 + b)
                if 0 <= x1 < self.x and 0 <= y1 < self.y:
                    if self.pixels[x1, y1] != (255, 255, 255):
                        return (x1, y1)
                    else:
                        return (x, y)
                else:
                    return (x, y)
            else:
                x1 = x + 1
                y1 = int(k * x1 + b)
                if 0 <= x1 < self.x and 0 <= y1 < self.y:
                    if self.pixels[x1, y1] != (255, 255, 255):
                        return (x1, y1)
                    else:
                        return (x, y)
                else:
                    return (x, y)
        else:
            if a == 0:
                if 0 <= x + 1 < self.x and 0 <= y < self.y:
                    if self.pixels[x + 1, y] != (255, 255, 255):
                        return (x + 1, y)
                    else:
                        return (x, y)
                else:
                    return (x, y)
            elif a == 180:
                if 0 <= x - 1 < self.x and 0 <= y < self.y:
                    if self.pixels[x - 1, y] != (255, 255, 255):
                        return (x - 1, y)
                    else:
                        return (x, y)
                else:
                    return (x, y)
            elif a == 90:
                if 0 <= x < self.x and 0 <= y - 1 < self.y:
                    if self.pixels[x, y - 1] != (255, 255, 255):
                        return (x, y - 1)
                    else:
                        return (x, y)
                else:
                    return (x, y)
            else:
                if 0 <= x < self.x and 0 <= y + 1 < self.y:
                    if self.pixels[x, y + 1] != (255, 255, 255):
                        return (x, y + 1)
                    else:
                        return (x, y)
                else:
                    return (x, y)

    def pixel(self, x, y):
        if self.pixels[x, y] == (34, 177, 76):
            return True
        else:
            return False


if __name__ == '__main__':
    a = MainImage("map/level1.png")
    print(a.step(cordinat=(20, 20), a=0))
