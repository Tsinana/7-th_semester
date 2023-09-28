import cv2 as cv
import numpy as np


class Thick_red_cross:
  @classmethod
  def start(cls):
    img = cv.imread('other\duck.PNG')
    cv.namedWindow('Display window', cv.WINDOW_NORMAL | cv.WINDOW_FREERATIO | cv.WINDOW_GUI_EXPANDED)

    # Высота и ширина исходной картинки
    height = img.shape[0]
    width = img.shape[1]

    centerPixel = img[int(height / 2), int(width / 2)]

    max_value = centerPixel[0]
    color = (255, 0, 0)
    if centerPixel[1] > max_value:
      max_value = centerPixel[1]
      color = (0, 255, 0)
    if centerPixel[2] > max_value:
      color = (0, 0, 255)

    # верхняя левая и нижняя правая точка первого прямоугольника
    start_point1 = (int(width / 2 - 20), int(height / 2 - height / 4))
    end_point1 = (int(width / 2 + 20), int(height / 2 + height / 4))

    # верхняя левая и нижняя правая точка второго прямоугольника
    start_point = (int(width / 2 - height / 4), int(height / 2 - 20))
    end_point = (int(width / 2 + height / 4), int(height / 2 + 20))

    # рисуем прямоугольники
    img = cv.rectangle(img, start_point, end_point, color, -1)
    img = cv.rectangle(img, start_point1, end_point1, color, -1)

    cv.imshow('Display window', img)
    cv.waitKey(0)
    cv.destroyAllWindows()
