import random
import pygame as pg


class World:
    def __init__(self, size):
        self.size = size
        self.present = 0
        self.future = 1
        self.cell_width = 5
        self.root = pg.Surface((self.size[0]*self.cell_width, self.size[1]*self.cell_width))
        self.map = [[[0 for i in range(size[0])] for j in range(size[1])],
                    [[0 for i in range(size[0])] for j in range(size[1])]]
        self.random_filling(round(self.size[0]*self.size[1]*0.05))

    def random_filling(self, num):
        while num != 0:
            x, y = random.randint(0, self.size[0]-1), random.randint(0, self.size[1]-1)
            if not self.map[self.present][y][x]:
                self.map[self.present][y][x] = 1
                num -= 1

    def __compute_filling_cells_around(self, x, y):
        counter = 0
        for i in range(y-1, y+2):
            if 0 <= i < self.size[1]:
                for j in range(x-1, x+2):
                    if 0 <= j < self.size[0]:
                        if self.map[self.present][i][j]:
                            counter += 1
        counter -= self.map[self.present][y][x]
        return counter

    def make_a_move(self):
        for y in range(0, self.size[1]):
            for x in range(0, self.size[0]):
                neighbours = self.__compute_filling_cells_around(x, y)
                self.map[self.future][y][x] = neighbours
                if neighbours == 3:
                    self.map[self.future][y][x] = 1
                elif neighbours == 2 and self.map[self.present][y][x]:
                    self.map[self.future][y][x] = 1
                else:
                    self.map[self.future][y][x] = 0
        self.present, self.future = self.future, self.present

    def drawing(self):
        self.root.fill((255, 255, 255, 255))
        for y in range(0, self.size[1]):
            for x in range(0, self.size[0]):
                if self.map[self.present][y][x]:
                    pg.draw.rect(self.root, (0, 0, 0, 0), (x*self.cell_width, y*self.cell_width,
                                                           self.cell_width, self.cell_width))

    def print(self):
        for y in self.map[self.present]:
            for x in y:
                print(x, end='')
            print()


# world = World((50, 50))
# world.random_filling(1000)
# world.print()
# print()
# world.make_a_move()
# world.print()
