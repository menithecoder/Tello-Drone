import speech_re as sr
import time
#import gun_fire as gf

def get_rec():
    word=sr.voice_t_text()

    time.sleep(2)
    print(word)






    lr, fb, ud, yv,tl = 0, 0, 0, 0,0
    speed = 40
    if "fire" in word.lower() or "hamas" in word.lower() :
        gf.fire(1)

        tl = 3
        return [lr, fb, ud, yv, tl]
    if word.lower() == "hamas we are coming for you":
        gf.fire(1)
        tl = 4
        return [lr, fb, ud, yv, tl]


    if word.lower()=="left":
        lr = -speed
    elif word.lower()=="right":
        lr = speed

    if word.lower()=="forward":
        fb = speed
    elif word.lower()=="backward":
        fb = -speed

    if word.lower()=="up":
        ud = speed
    elif word.lower()=="down":
        ud = -speed

    if word.lower()=="turn left":
        yv = -speed - 10
    elif word.lower()=="turn right":
        yv = speed + 10

    if word.lower()=="land":
        tl=2
    if word.lower()=="take off":
        tl=1
    #if lr == 0 and fb == 0 and ud == 0 and yv == 0 and tl == 0:
        #get_rec()
    return [lr,fb,ud,yv,tl]

if __name__ =='__main__':
    while True:
        get_rec()
