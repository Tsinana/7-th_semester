import numpy as np
import cv2 as cv


class RedObjectTracking:
  @classmethod
  def class_work(cls):
    cap = cv.VideoCapture(0)
    kernel = np.ones((5, 5), np.uint8)
    while (1):
      ret, frame = cap.read()
      if ret == True:
        hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        # создание маски для красных объектов
        min_p = (0, 116, 186)
        max_p = (20, 255, 255)
        mask = cv.inRange(hsv_frame, min_p, max_p)

        # морфологические операции
        processed_mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
        processed_mask = cv.morphologyEx(processed_mask, cv.MORPH_CLOSE, kernel)

        moments = cv.moments(processed_mask, 1)
        dM01 = moments['m01']
        dM10 = moments['m10']
        dArea = moments['m00']

        if dArea > 1000:
          x = int(dM10 / dArea)
          y = int(dM01 / dArea)
          cv.circle(frame, (x, y), 10, (0, 0, 255), -1)

          contours, _ = cv.findContours(processed_mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

          max_cnt = cv.contourArea(contours[0])
          max_cnt_obj = contours[0]
          for cnt in contours:
            if max_cnt < cv.contourArea(cnt):
              max_cnt = cv.contourArea(cnt)
              max_cnt_obj = cnt
          x, y, w, h = cv.boundingRect(max_cnt_obj)

          cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 0), 5)

        cv.imshow('img', frame)
        cv.imshow('mask', mask)
        cv.imshow('processed_mask', processed_mask)

        k = cv.waitKey(30) & 0xff
        if k == 27:
          break
      else:
        break
