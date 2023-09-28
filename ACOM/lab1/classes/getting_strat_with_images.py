import cv2 as cv
from matplotlib import pyplot as plt


class Getting_start_with_images:
  @classmethod
  def start(cls):
    img = cv.imread('other\duck.PNG')

    cv.namedWindow('WINDOW_AUTOSIZE', cv.WINDOW_AUTOSIZE)
    cv.namedWindow('WINDOW_NORMAL ', cv.WINDOW_NORMAL)
    cv.namedWindow('WINDOW_GUI_EXPANDED', cv.WINDOW_GUI_EXPANDED)
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    titles = ['BGR',
              'HSV']
    images = [img, hsv]

    # cv.imshow('WINDOW_AUTOSIZE', img1)
    # cv.imshow('WINDOW_NORMAL ', img2)
    # cv.imshow('WINDOW_GUI_EXPANDED', img3)

    for i in range(2):
      plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
      plt.title(titles[i])
      plt.xticks([]), plt.yticks([])
    plt.show()

    cv.waitKey(0)
    cv.destroyAllWindows()
