import numpy as np
import cv2 as cv
import argparse


class RedObjectTracking:
  @classmethod
  def class_work(cls):
    def nothing(x):
      pass

    cv.namedWindow("setup")
    cv.createTrackbar("low_h", "setup", 0, 180, nothing)
    cv.createTrackbar("low_s", "setup", 0, 255, nothing)
    cv.createTrackbar("low_v", "setup", 0, 255, nothing)
    cv.createTrackbar("up_h", "setup", 180, 180, nothing)
    cv.createTrackbar("up_s", "setup", 255, 255, nothing)
    cv.createTrackbar("up_v", "setup", 255, 255, nothing)
    cap = cv.VideoCapture(0)
    kernel = np.ones((5, 5), np.uint8)
    while (1):
      ret, frame = cap.read()
      if ret == True:
        low_h = cv.getTrackbarPos('low_h', 'setup')
        low_s = cv.getTrackbarPos('low_s', 'setup')
        low_v = cv.getTrackbarPos('low_v', 'setup')
        up_h = cv.getTrackbarPos('up_h', 'setup')
        up_s = cv.getTrackbarPos('up_s', 'setup')
        up_v = cv.getTrackbarPos('up_v', 'setup')
        #0 45 200
        #20 255 255
        min_p1 = (0, 116, 186)
        max_p1 = (20, 255, 255)
        min_p = (low_h, low_s, low_v)
        max_p = (up_h, up_s, up_v)
        hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        mask = cv.inRange(hsv_frame, min_p1, max_p1)

        opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
        closing = cv.morphologyEx(opening, cv.MORPH_CLOSE, kernel)
        # площадь
        moments = cv.moments(closing,1)
        dM01 = moments['m01']
        dM10 = moments['m10']
        dArea = moments['m00']
        if dArea > 100:
          x = int(dM10 / dArea)
          y = int(dM01 / dArea)
          cv.circle(frame, (x, y), 10, (0, 0, 255), -1)

        cv.imshow('img', frame)
        cv.imshow('mask', mask)
        cv.imshow('threshold_mask', closing)
        k = cv.waitKey(30) & 0xff
        if k == 27:
          break
      else:
        break

  @classmethod
  def meanshift(cls):
    cap = cv.VideoCapture(0)
    # take first frame of the video
    ret, frame = cap.read()
    # setup initial location of window
    x, y, w, h = 300, 200, 100, 50  # simply hardcoded the values
    track_window = (x, y, w, h)
    # set up the ROI for tracking
    roi = frame[y:y + h, x:x + w]
    hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
    lower_red = np.array([100, 60, 32])
    upper_red = np.array([180, 255, 255])

    mask = cv.inRange(hsv_roi, lower_red, upper_red)
    roi_hist = cv.calcHist([hsv_roi], [0], mask, [180], [0, 180])
    cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX)
    # Setup the termination criteria, either 10 iteration or move by at least 1 pt
    term_crit = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)
    while (1):
      ret, frame = cap.read()
      if ret == True:
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        dst = cv.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
        # apply meanshift to get the new location
        ret, track_window = cv.meanShift(dst, track_window, term_crit)
        # Draw it on image
        x, y, w, h = track_window
        img2 = cv.rectangle(frame, (x, y), (x + w, y + h), 255, 2)
        cv.imshow('img2', img2)
        k = cv.waitKey(30) & 0xff
        if k == 27:
          break
      else:
        break

  @classmethod
  def сamshift(cls):
    cap = cv.VideoCapture(0)
    # take first frame of the video
    ret, frame = cap.read()
    # setup initial location of window
    x, y, w, h = 300, 200, 100, 50  # simply hardcoded the values
    track_window = (x, y, w, h)
    # set up the ROI for tracking
    roi = frame[y:y + h, x:x + w]
    hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)

    lower_red = np.array([100, 60, 32])
    upper_red = np.array([180, 255, 255])

    mask = cv.inRange(hsv_roi, lower_red, upper_red)
    roi_hist = cv.calcHist([hsv_roi], [0], mask, [180], [0, 180])
    cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX)
    # Setup the termination criteria, either 10 iteration or move by at least 1 pt
    term_crit = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)
    while (1):
      ret, frame = cap.read()
      if ret == True:
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        dst = cv.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
        # apply camshift to get the new location
        ret, track_window = cv.CamShift(dst, track_window, term_crit)
        # Draw it on image
        pts = cv.boxPoints(ret)
        pts = np.int0(pts)
        img2 = cv.polylines(frame, [pts], True, 255, 2)
        cv.imshow('img2', img2)
        cv.imshow('mask', mask)
        k = cv.waitKey(30) & 0xff
        if k == 27:
          break
      else:
        break
