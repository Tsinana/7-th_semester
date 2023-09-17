import cv2 as cv
import numpy as np


class Task6:
  @classmethod
  def start(cls):
    img = cv.imread('other\pussInBoots.PNG')
    cv.namedWindow('Display window', cv.WINDOW_NORMAL | cv.WINDOW_FREERATIO | cv.WINDOW_GUI_EXPANDED)

    height = img.shape[0]
    width = img.shape[1]

    start_point1 = (int(width / 2 - 20), int(height / 2 - height / 4))
    end_point1 = (int(width / 2 + 20), int(height / 2 + height / 4))
    color = (0, 0, 255)
    thickness = 4

    start_point = (int(width / 2 - height / 4), int(height / 2 - 20))
    end_point = (int(width / 2 + height / 4), int(height / 2 + 20))

    cat1 = img[start_point1[1]:end_point1[1], start_point1[0]:end_point1[0]].copy()
    cat2 = img[start_point[1]:end_point[1], start_point[0]:end_point[0]].copy()
    cat1 = cv.blur(cat1, (10, 10))
    cat2 = cv.blur(cat2, (10, 10))

    img = cv.rectangle(img, start_point, end_point, color, thickness)
    img = cv.rectangle(img, start_point1, end_point1, color, thickness)

    img[start_point1[1]:end_point1[1], start_point1[0]:end_point1[0]] = cat1
    img[start_point[1]:end_point[1], start_point[0]:end_point[0]] = cat2

    cv.imshow('Display window', img)
    cv.waitKey(0)
    cv.destroyAllWindows()
