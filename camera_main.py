# Author: Kai Zhang
# Stevens Institute of Technology


import cv2
import time # create a file name with the current data & time
import sys
global timer
import threading

def main():
    global num

    #cap=cv2.VideoCapture(0) # 0 means the camera0

    if cap.isOpened():
        # get a frame
        ret,frame=cap.read()
        #print(ret)
        #print(frame)
    else:
        ret=False

    # create a filename with the time
    filename=time.strftime("/home/kai/kevin/%Y%m%d-%H%M%S.jpeg", time.localtime())
    cv2.imwrite(filename, frame)
    num+=1
    if num==10:
        cap.release()
        cv2.destroyAllWindows()
        sys.exit()
    timer=threading.Timer(1, main)
    timer.start()
    
if __name__ == "__main__":
    num=0
    cap=cv2.VideoCapture(0)
    timer=threading.Timer(1, main)
    timer.start()