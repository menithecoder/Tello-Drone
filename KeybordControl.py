import KeyPress as kp
from djitellopy import tello
import time
import cv2
import basic as bc
import get_imput_func as get_f
import get_record as get_r
import threading as tr
import militery_sight as ms
import queue
import threading
import mouse_detector as md



me=tello.Tello()
me.connect()
me.streamon()
me.get_battery()
me.takeoff()



flip_forward_event = tr.Event()


def video_capture():
    global num
    while True:
        img = me.get_frame_read().frame
        img = cv2.resize(img, (900, 700))
        if flip_forward_event.is_set():
            color=(20,0,255)
        else:color=(0,255,0)
        img=ms.sight(50,50,img,color)
        cv2.imshow("image", img)
        cv2.waitKey(1)
def drone_control():
    while True:

        values_r = get_r.get_rec()  # Assuming get_r is defined somewhere
        if values_r[4] == 1:
            me.takeoff()
        elif values_r[4] == 2:
            me.land()
        elif values_r[4] == 3:
            flip_forward_event.set()
            me.flip_forward()
            flip_forward_event.clear()
        elif values_r[4] == 4:
            me.flip_left()
         #   me.flip_right()





        me.send_rc_control(values_r[0], values_r[1], values_r[2], values_r[3])

        time.sleep(1)
        me.send_rc_control(0, 0, 0, 0)






video_thread = tr.Thread(target=video_capture)
drone_thread = tr.Thread(target=drone_control)


video_thread.start()
drone_thread.start()

video_thread.join()
drone_thread.join()


