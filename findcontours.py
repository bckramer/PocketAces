import cv2
import numpy as np
from areaOfInterest import *
from Utils import *
import time

def findElementInImage(image, structuringElements, cardValues):
    i = 0
    k = 0
    for strel in structuringElements:
        erosion = cv2.erode(image, strel, iterations=1)
        # J and 10 get mixed up a lot when looking for the value of a card.
        # This fixes that. Hopefully the root cause can be found, but for now, this works
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
            if i == 1 or i == 8:
                k = i
            else:
                return i
        i = i + 1
    if k == 0:
        k = -2
    return k

def determinePotSize(image, structuringElements, dollar):
    boxes = findROIs(image, dollar)
    for box in boxes:
        i = 0
        for strel in structuringElements:
            erosion = cv2.erode(box.image, strel, iterations=1)
            y,x = erosion.shape[:2]
            erosion = erosion[0:y, 10:x]
            im, contours, hierarchy = cv2.findContours(erosion, cv2.RETR_TREE,
                                                        cv2.CHAIN_APPROX_SIMPLE)
            if len(contours) > 0:
                # This is necessary because 0s can conjoin.
                # This could be volatile, however to if there
                # are issues, look here
                if len(contours) == 2:
                    box.num = "00"
                else:
                    box.num = i
            i = i + 1
    numberReps = ""
    for box in boxes:
        if box.num != -1:
            numberReps = numberReps + str(box.num)
    if len(numberReps) == 0:
        return -1
    return numberReps

def findROIs(image, strel):
    boxes = []
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
        image = image[0:y1, x + 11:y1]
        im, contours, hierarchy = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            if cv2.contourArea(contour) > 0:
                areaOfInterest = makeNew(x, y, x + w, y + h, -1)
                areaOfInterest.image = image[areaOfInterest.y1:areaOfInterest.y2, areaOfInterest.x1:areaOfInterest.x2]
                areaOfInterest.image = addBlackBorder(areaOfInterest.image)
                areaOfInterest.image = binarizeAndErode(areaOfInterest.image, 0, 0, 150, True)
                boxes.append(areaOfInterest)
        boxes = insertion_sort(boxes)
        boxes.reverse()
        # for i in range(0, len(boxes)):
        #     cv2.imshow("box" + str(i), boxes[i].image)
    return boxes
