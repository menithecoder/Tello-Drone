import cv2




def sight(x,y,img,color):
    cv2.line(img,((img.shape[1]//2)-x,(img.shape[0]//2)-y),((img.shape[1]//2)-x+15,(img.shape[0]//2)-y),color,1)
    cv2.line(img, ((img.shape[1] // 2) - x, (img.shape[0] // 2) - y),
             ((img.shape[1] // 2) - x , (img.shape[0] // 2) - y+15), color, 1)

    cv2.line(img, ((img.shape[1] // 2) - x, (img.shape[0] // 2) + y),
             ((img.shape[1] // 2) - x + 15, (img.shape[0] // 2) + y), color, 1)
    cv2.line(img, ((img.shape[1] // 2) - x, (img.shape[0] // 2) + y),
             ((img.shape[1] // 2) - x, (img.shape[0] // 2) + y - 15), color, 1)

    cv2.line(img, ((img.shape[1] // 2) + x, (img.shape[0] // 2) + y),
             ((img.shape[1] // 2) + x - 15, (img.shape[0] // 2) + y), color, 1)
    cv2.line(img, ((img.shape[1] // 2) + x, (img.shape[0] // 2) + y),
             ((img.shape[1] // 2) + x, (img.shape[0] // 2) + y - 15), color, 1)

    cv2.line(img, ((img.shape[1] // 2) + x, (img.shape[0] // 2) - y),
             ((img.shape[1] // 2) + x - 15, (img.shape[0] // 2) - y), color, 1)
    cv2.line(img, ((img.shape[1] // 2) + x, (img.shape[0] // 2) - y),
             ((img.shape[1] // 2) + x, (img.shape[0] // 2) - y + 15), color, 1)
    ####################################################################################
    cv2.line(img,((img.shape[1]//2)-80,img.shape[0]//2),((img.shape[1]//2)-20,img.shape[0]//2),color,1)

    cv2.line(img, ((img.shape[1] // 2) + 80, img.shape[0] // 2), ((img.shape[1] // 2) + 20, img.shape[0] // 2),
             color, 1)

    cv2.line(img, ((img.shape[1] // 2) , (img.shape[0] // 2)-80), ((img.shape[1] // 2), (img.shape[0] // 2)-20),
             color, 1)

    cv2.line(img, ((img.shape[1] // 2), (img.shape[0] // 2) + 80), ((img.shape[1] // 2), (img.shape[0] // 2) + 20),
             color, 1)

    return img




def open_camera():
    vid=cv2.VideoCapture(0)
    while True:
        ret,img=vid.read()
        img=cv2.resize(img,(615,480))
        color=(20,0,255)

        s_img=sight(50,50,img,color)
        cv2.imshow("Video",s_img)
        cv2.waitKey(1)




if __name__=="__main__":
    open_camera()
