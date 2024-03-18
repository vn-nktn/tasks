import unittest
import math
from task2 import Circle, Triangle


class TestFigure(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(radius=5)
        self.assertAlmostEqual(circle.area(), math.pi * 5**2, places=2)

    def test_triangle_area(self):
        triangle = Triangle(a=3, b=4, c=5)
        self.assertAlmostEqual(triangle.area(), 6.0, places=2)

    def test_triangle_is_right_triangle(self):
        triangle = Triangle(a=3, b=4, c=5)
        self.assertTrue(triangle.is_right_triangle())

    def test_triangle_is_not_right_triangle(self):
        triangle = Triangle(a=1, b=2, c=3)
        self.assertFalse(triangle.is_right_triangle())


if __name__ == '__main__':
    unittest.main()
