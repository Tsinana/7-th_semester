import cv2 as cv
import numpy as np
from classes.my_gaussian_blur import MyGaussianBlur
from matplotlib import pyplot as plt


if __name__ == '__main__':
    img = cv.imread('other\duck.png')
    cv.namedWindow('Display window', cv.WINDOW_NORMAL | cv.WINDOW_FREERATIO | cv.WINDOW_GUI_EXPANDED)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)


    # kernal = MyGaussianBlur.gaussian_filter((5, 5), 1)
    # # kernal = np.zeros((5, 5), np.float32)
    # # for i in range(5):
    # #     # for j in range(5):
    # #     kernal[i, 2] = 0.2
    # img_hsv_blur1 = MyGaussianBlur.convolution(img_hsv, kernal)

    blurred_img = cv.GaussianBlur(img,(5,5),0)




    titles = ['Image','Blurred image']

    images = [img, blurred_img]


    for i in range(2):
        plt.subplot(1, 2, i + 1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()


    cv.destroyAllWindows()