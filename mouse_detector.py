from pynput.mouse import Listener, Button
from threading import Thread
import queue
#import gun_fire
# Function to be called when the mouse is moved
from djitellopy import tello
import gun_fire
m_x=960
m_y=540
j_x=960/100
j_y=540/100


me=tello.Tello()
me.connect()
me.streamon()
me.get_battery()
me.takeoff()


def on_move(x, y):
    lr, fb = 0, 0
    lr = int((x - m_x) / j_x)
    fb = int((y - m_y) / j_y)
    me.send_rc_control(lr,fb,0,0)




# Function to be called when a mouse button is clicked
def on_click(x, y, button):
    a=1

    if button == Button.left:
        gun_fire.fire(1)

    elif button == Button.right:
        gun_fire.fire(2)

            # Perform actions for right click here

# Function to be called when the mouse wheel is scrolled
def on_scroll(x, y, dx, dy):
    ud=0
    if dy > 0:
        ud=20
        me.send_rc_control(0, 0, ud, 0)



        # Perform actions for scrolling up
    elif dy < 0:
        ud=-20
        me.send_rc_control(0, 0, ud, 0)

        # Perform actions for scrolling down

# Function to start listening for mouse movement
def start_mouse_movement_listener():
    with Listener(on_move=on_move) as listener:
        listener.join()  # Start listening for mouse movement

# Function to start listening for mouse clicks
def start_mouse_click_listener():
    with Listener(on_click=on_click) as listener:
        listener.join()  # Start listening for mouse clicks

# Function to start listening for mouse scroll
def start_mouse_scroll_listener():
    with Listener(on_scroll=on_scroll) as listener:
        listener.join()  # Start listening for mouse scroll





movement_thread = Thread(target=start_mouse_movement_listener )
click_thread = Thread(target=start_mouse_click_listener)
scroll_thread = Thread(target=start_mouse_scroll_listener)

movement_thread.start()
click_thread.start()
scroll_thread.start()




