import numpy as np
import cv2
from PIL import ImageGrab
from ScreenRead import *
from Utils import *

# VERY IMPORTANT: Without it, the entire screen will not be captured
from ctypes import windll
user32 = windll.user32
user32.SetProcessDPIAware()

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (1920,1080))
font = cv2.FONT_HERSHEY_SIMPLEX
while(True):

    frame = np.array(ImageGrab.grab())

    values = getAllValues()
    print(values[1])
    print (values[3])
    cv2.putText(frame, getReadableCard(values[0], values[1]), (0, 600), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, getReadableCard(values[2], values[3]), (1000, 600), font, 1, (0, 255, 0), 2, cv2.LINE_AA)

    out.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


out.release()