import cv2
import potsizeobj
from Utils import *

def findElementInImage(image, structuringElements, cardValues):
    i = 0
    k = 0
    for strel in structuringElements:
        erosion = cv2.erode(image, strel, iterations=1)
        # J and 10 get mixed up a lot when looking for the value of a card.
        # This fixes that. Hopfully the root cause can be found, but for now, this works
        if (cardValues):
            row, col = erosion.shape
            erosion = erosion[0:col, 0:row - 20]
        im, contours, hierarchy = cv2.findContours(erosion, cv2.RETR_TREE,
                                                   cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) == 1:
            # 3s and eights get confused. Right now this is
            # the best solution. Modifying the 3 structuring
            # element fixes the 8 issues, but causes 2s to be
            # confused with 3s
            if i == 1:
                k = i
            else:
                return i
        i = i + 1
    if k == 0:
        k = -2
    return k

def determinePotSize(image, structuringElements):
    i = -1
    potSizeObjs = []
    xCoords = []
    for strel in structuringElements:
        if i == -1:
            erosion = cv2.erode(image, strel, iterations=1)
            im, contours, hierarchy = cv2.findContours(erosion, cv2.RETR_TREE,
                                                       cv2.CHAIN_APPROX_SIMPLE)
            if len(contours) > 0:
                x = 10000
                for contour in contours:
                    x0, y0, w0, h0 = cv2.boundingRect(contour)
                    if x0 < x:
                        x = x0
                x1, y1 = image.shape
                image = image[0:y1, x + 9:y1]
            cv2.imshow("image", image)
        else:
            erosion = cv2.erode(image, strel, iterations=1)
            im, contours, hierarchy = cv2.findContours(erosion, cv2.RETR_TREE,
                                                   cv2.CHAIN_APPROX_SIMPLE)
            for contour in contours:
                x, y, w, h = cv2.boundingRect(contour)
                potSizeObj = potsizeobj.makeNew(x, i)
                potSizeObjs.append(potSizeObj)
                xCoords.append(x)
        i = i + 1
    numberReps = ""
    xCoords.sort()
    for xCoord in xCoords:
        for obj in potSizeObjs:
            if xCoord == obj.xCoord and xCoord != 0:
                numberReps += str(obj.number)
    return numberReps
