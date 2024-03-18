import math
from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        '''Вычисление площади круга по радиусу'''
        return math.pi * self.radius ** 2


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        '''Вычисление площади треугольника по трем сторонам через формулу Герона'''
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def is_right_triangle(self):
        '''Проверка на прямой прямоугольник по теореме Пифагора'''
        sides = sorted([self.a, self.b, self.c])
        return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2
