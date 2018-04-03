import cv2
import potsizeobj
import numpy as np
from rectangle import *
from Utils import *
import time

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
            if i == 0:
                cv2.drawContours(erosion, contours, -1, (255, 255, 0), 3)
                cv2.imshow("0", erosion)
            elif i == 1:
                cv2.drawContours(erosion, contours, -1, (255, 255, 0), 3)
                cv2.imshow("1", erosion)
            elif i == 2:
                cv2.drawContours(erosion, contours, -1, (255, 255, 0), 3)
                cv2.imshow("2", erosion)
            elif i == 3:
                cv2.drawContours(erosion, contours, -1, (255, 255, 0), 3)
                cv2.imshow("3", erosion)
            elif i == 4:
                cv2.drawContours(erosion, contours, -1, (255, 255, 0), 3)
                cv2.imshow("4", erosion)
            elif i == 5:
                cv2.drawContours(erosion, contours, -1, (255, 255, 0), 3)
                cv2.imshow("5", erosion)
            elif i == 6:
                cv2.imshow("6-1", erosion)
                cv2.drawContours(erosion, contours, -1, (255, 255, 0), 3)
                cv2.imshow("6", erosion)
            elif i == 7:
                cv2.drawContours(erosion, contours, -1, (255, 255, 0), 3)
                cv2.imshow("7", erosion)
            elif i == 8:
               # cv2.drawContours(erosion, contours, -1, (128, 255, 0), 3)
                cv2.imshow("8", erosion)
            elif i == 9:
                cv2.drawContours(erosion, contours, -1, (255, 255, 0), 3)
                cv2.imshow("9", erosion)
            if len(contours) > 0:
                for contour in contours:
                    x, y, w, h = cv2.boundingRect(contour)
                    box.num = i
            i = i + 1
    numberReps = ""
    for box in boxes:
        if box.num != -1:
            numberReps = numberReps + str(box.num)
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
        cv2.imshow("image", image)
        im, contours, hierarchy = cv2.findContours(image, cv2.RETR_TREE,
                                                           cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            if cv2.contourArea(contour) > 0:
                rectangle = makeNew(x, y, x + w, y + h, -1)
                rectangle.image = image[rectangle.y1:rectangle.y2, rectangle.x1:rectangle.x2]
                rectangle.image = addBlackBorder(rectangle.image)
                rectangle.image = binarizeAndErode(rectangle.image, 0, 0, 150, True)
                boxes.append(rectangle)
        boxes = insertion_sort(boxes)
        boxes.reverse()
    return boxes
