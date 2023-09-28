import numpy as np
import cv2 as cv
import argparse


class Test:
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
    cap = cv.imread("rgb.jpg")


    low_h = cv.getTrackbarPos('low_h', 'setup')
    low_s = cv.getTrackbarPos('low_s', 'setup')
    low_v = cv.getTrackbarPos('low_v', 'setup')
    up_h = cv.getTrackbarPos('up_h', 'setup')
    up_s = cv.getTrackbarPos('up_s', 'setup')
    up_v = cv.getTrackbarPos('up_v', 'setup')

    min_p = (low_h, low_s, low_v)
    max_p = (up_h, up_s, up_v)
    hsv_frame = cv.cvtColor(cap, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv_frame, min_p, max_p)
    cv.imshow('hsv', hsv_frame)
    cv.imshow('cap', cap)
    cv.imshow('mask', mask)
    cv.waitKey(0)
