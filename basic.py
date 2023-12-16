from djitellopy import tello
from time import sleep
import cv2


me=tello.Tello()

me.connect()
def opencamera():
    me.streamon()
    while True:
        img = me.get_frame_read().frame
        img = cv2.resize(img, (640, 480))
        cv2.imshow("image", img)
        cv2.waitKey(1)




print(me.get_battery())