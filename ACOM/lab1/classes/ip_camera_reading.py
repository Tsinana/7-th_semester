import cv2


class Ip_camera_reading:
  @classmethod
  def start(cls):
    url = 'http://192.168.0.101:8080/video'
    cap = cv2.VideoCapture(url)

    while cap.isOpened():
      ret, frame = cap.read()
      if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

      cv2.imshow('Phone camera', frame)

      if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cap.release()
    cv2.destroyAllWindows()
