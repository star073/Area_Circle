class Restangle:
    def __init__(self,a, b):
        self.a = a
        self.b = b
    def getArea(self):
        return self.a * self.b

class Square:
    def __init__(self, a):
        self.a = a
    def getArea_square(self):
        return self.a ** 2

class Circle:
    def __init__(self, r):
        self.r = r

    def getArea_Circle(self):
        return self.r ** 2 * 3.14
