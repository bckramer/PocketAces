class Rectangle(object):
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    position = 0
    num = 0

def makeNew(x1, y1, x2, y2, position, num):
    rectangle = Rectangle()
    rectangle.x1 = x1
    rectangle.y1 = y1
    rectangle.x2 = x2
    rectangle.y2 = y2
    rectangle.position = position
    rectangle.num = num

    return rectangle