import cv2 as cv
import numpy as np


class Thin_red_cross:
  @classmethod
  def start(cls):
    img = cv.imread('other\duck.PNG')
    cv.namedWindow('Display window', cv.WINDOW_NORMAL | cv.WINDOW_FREERATIO | cv.WINDOW_GUI_EXPANDED)

    # Высота и ширина исходной картинки
    height = img.shape[0]
    width = img.shape[1]

    # верхняя левая и нижняя правая точка первого прямоугольника
    start_point1 = (int(width / 2 - 20), int(height / 2 - height / 4))
    end_point1 = (int(width / 2 + 20), int(height / 2 + height / 4))
    # цвет прямоугольника
    color = (0, 0, 255)

    # верхняя левая и нижняя правая точка второго прямоугольника
    start_point = (int(width / 2 - height / 4), int(height / 2 - 20))
    end_point = (int(width / 2 + height / 4), int(height / 2 + 20))

    # ДО рисования прямоугольников копируем область
    blur_zone = img[start_point[1]:end_point[1], start_point[0]:end_point[0]].copy()
    # наносим размытие
    blur_zone = cv.blur(blur_zone, (10, 10))

    # рисуем прямоугольники
    img = cv.rectangle(img, start_point, end_point, color, 4)
    img = cv.rectangle(img, start_point1, end_point1, color, 2)

    # вставляем нашу размытую зону
    img[start_point[1]:end_point[1], start_point[0]:end_point[0]] = blur_zone

    cv.imshow('Display window', img)
    cv.waitKey(0)
    cv.destroyAllWindows()
