import cv2


class Working_with_video_parameters:
  @classmethod
  def start(cls):
    cap = cv2.VideoCapture(0)
    cap.set(3, 4000)
    cap.set(4, 3120)
    cap.set(22, -1000)
    while True:
      ret, frame = cap.read()

      cv2.imshow('frame', frame)
      if cv2.waitKey(1) & 0xFF == 27:
        break

    cap.release()
    cv2.destroyAllWindows()
