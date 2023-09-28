import numpy as np
import cv2 as cv


class Working_with_vidoe:
  @classmethod
  def saving_a_video(cld):
    cap = cv.VideoCapture(0)
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
    while cap.isOpened():
      ret, frame = cap.read()
      if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

      out.write(frame)
      cv.imshow('frame', frame)
      if cv.waitKey(1) == ord('q'):
        break

    cap.release()
    out.release()
    cv.destroyAllWindows()

  @classmethod
  def playing_video_from_file(cls):
    cap = cv.VideoCapture('output.avi')
    while cap.isOpened():
      ret, frame = cap.read()
      if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

      cv.imshow('frame', frame)
      if cv.waitKey(1) == ord('q'):
        break
    cap.release()
    cv.destroyAllWindows()
