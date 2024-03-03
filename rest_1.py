from rest import Restangle, Square, Circle
rest_1 = Restangle(5,10)
rest_2 = Restangle(2,4)

print(rest_1.getArea())
print(rest_2.getArea())

square_1 = Square(5)
square_2 = Square(2)

print(square_1.getArea_square(),"\n",square_2.getArea_square())

figures = [rest_1, rest_2, square_1, square_2]
for figure in figures:
    if isinstance(figure, Square):
        print(figure.getArea_square())
    else:
        print(figure.getArea())

r = Circle(5)

print(r.getArea_Circle())



