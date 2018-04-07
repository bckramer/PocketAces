import numpy as np

class areaOfInterest(object):
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    num = 0
    image = np.ones((1, 1), np.uint8)


def makeNew(x1, y1, x2, y2, num):
    rectangle = areaOfInterest()
    rectangle.x1 = x1
    rectangle.y1 = y1
    rectangle.x2 = x2
    rectangle.y2 = y2
    rectangle.num = num

    return rectangle


def insertion_sort(l):
    for i in range(1, len(l)):
        j = i-1
        key = l[i].x1
        while (l[j].x1 > key) and (j >= 0):
           l[j+1].x1 = l[j].x1
           j -= 1
        l[j+1].x1 = key
    return l
# credit: http://python3.codes/popular-sorting-algorithms/