import pygame as pg
from random import randint
import time

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

class Button:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pg.image.load('images/pixil-frame-0.png')
        self.image2 = pg.image.load('images/pixil-frame-0 (1).png')
        self.image3 = pg.image.load('images/pixil-frame-0 (2).png')
        self.image_rect = self.image.get_rect()
        self.image2_rect = self.image2.get_rect()
        self.image3_rect = self.image3.get_rect()
        self.rg = True
        self.rgp = 0
        """self.boom = [[],[],[],[],[],[]]
        for i in range():
            self.boom[i] = pg.image.load(self.boom[i])
            self.boom[i] = self.boom[i].get_rect()"""
    def draw(self): #функция для рисования 5 точек и проверка чтобы не накладывались
        self.pos = [[-50, -50], [-50, -50], [-50, -50], [-50, -50], [-50, -50]] #координаты точек
        self.ftime = [[-50, -50], [-50, -50], [-50, -50], [-50, -50], [-50, -50]] #временный список чтобы проверять накладку точек друг на друга
        self.direction = [[randint(-1,1), randint(-1,1)], [randint(-1,1), randint(-1,1)], [randint(-1,1), randint(-1,1)], [randint(-1,1), randint(-1,1)], [randint(-1,1), randint(-1,1)]]

        self.flag = [False, False, False, False, False] #если true то попал
        self.start = time.time()
        z = 0
        while z < 25: #проверка накладности, точек 5 и при проверке каждой с каждой 5**2 = 25
            for k in range(5):
                l = [randint(50, 590), randint(50, 310)]
                self.ftime[k] = l
            for k in range(5):
                for j in range(5):
                    if (self.ftime[k][0] - self.ftime[j][0])**2 + (self.ftime[k][1] - self.ftime[j][1])**2 > 10000 or (self.ftime[k][0] - self.ftime[j][0])**2 + (self.ftime[k][1] - self.ftime[j][1])**2 == 0:
                        z += 1
                    else:
                        z = 0
        self.pos = self.ftime
        for i in range(5): #рисуем 5 белых точек
            self.image_rect.center = self.pos[i]
            self.screen.blit(self.image, self.image_rect)
            pg.display.update()
    def exam(self, screen): #проверка на попадание
        for i in range(5): #после нажатия проверят каждую точку, попал ли
            r = (pg.mouse.get_pos()[0] - self.pos[i][0])**2 + (pg.mouse.get_pos()[1] - self.pos[i][1])**2
            if r <= 2500:
                self.flag[i] = True
                self.image2_rect.center = self.pos[i]
                self.screen.blit(self.image2, self.image2_rect)
                pg.display.update()
                self.pos[i] = [-10000, -10000]
        self.time = time.time() - self.start
    def colred(self, screen): #закрашивание всех непопавших точек в красный
        for i in range(5):
            if self.flag[i] == False:
                self.image3_rect.center = self.pos[i]
                self.screen.blit(self.image3, self.image3_rect)
        pg.display.update()
    def kill(self, screen): #очищение
        for i in range(5):
            pg.draw.circle(screen, black, self.pos[i], 50)
            self.pos[i] = [-10000, -10000]
        pg.display.update()
    def times(self): #вывод времени
        if False in self.flag:
            print("Lose: ", int(1000 * self.time), "ms")
        else:
            print("Nice: ", int(1000 * self.time), "ms")
    def update(self): #обновление движения
        self.screen.fill(black)
        for i in range(5):
            if self.pos[i][0] + 50 >= 640 or self.pos[i][0] - 50 <= 0: #проверка каждой точки на пересечение с границей
                self.direction[i][0] *= -1
            if self.pos[i][1] + 50 >= 360 or self.pos[i][1] - 50 <= 0:
                self.direction[i][1] *= -1
            self.pos[i][0] += self.direction[i][0]
            self.pos[i][1] += self.direction[i][1]
            for j in range(5): #проверка точек на пересечение друг с другом
                r = (self.pos[i][0] - self.pos[j][0]) ** 2 + (self.pos[i][1] - self.pos[j][1]) ** 2
                if r <= 10000 and r != 0:
                    self.direction[i][0] *= -1
                    self.direction[i][1] *= -1
                    self.direction[j][0] *= -1
                    self.direction[j][1] *= -1
            self.pos[i][0] += self.direction[i][0]
            self.pos[i][1] += self.direction[i][1]
            self.image_rect.center = self.pos[i]
            if self.flag[i] == False:
                self.screen.blit(self.image, self.image_rect)




