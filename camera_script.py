# Author: Kai Zhang
# Stevens Institute of Technology

import cv2
import time # create a file name with the current data & time
import sys
global timer
import threading

def pic_shot(num):

    cap=cv2.VideoCapture(0)
    
    if cap.isOpened():
        # get a frame
        ret,frame=cap.read()
    else:
        ret=False

    # create a filename with the time
    # change the directory to save pictures
    filename=time.strftime("/home/kai/kevin/%Y%m%d-%H%M%S.jpeg", time.localtime())
    # generate the picture
    cv2.imwrite(filename, frame)
    # take 10 pictures, then stop, waiting for next operation
    num+=1
    if num > 10:
        cap.release()
        cv2.destroyAllWindows()
        sys.exit()
        return 0

    timer=threading.Timer(1, pic_shot, (num,))
    timer.start()


def pic_shot_run():
    pic_shot(1)



    