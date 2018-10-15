# Author: Kai Zhang
# Stevens Institute of Technology

#import matplotlib.pyplot as plt
import time # create a file name with the current data & time
import sys
global timer
import threading
import cv2

def main():
    #cap=cv2.VideoCapture(0) # 0 means the camera0
    global num

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

    # 0xFF is a hexadecimal constant which is 11111111 in binary. By using bitwise AND (&) with this constant, it leaves only the last 8 bits of the original (in this case, whatever cv2.waitKey(0) is).
    # ord('q') returns an integer representing the Unicode code point of the ('q') when the argument is a unicode object, or value of the byte when argument is an 8-bit string. 
    #if cv2.waitKey(1)&0xFF == ord('q'):
        #cv2.imwrite("/opt/code/image/fangjian2.jpeg", frame)
        #break

    # uncomment to test whether the photo is captured

    #img1=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #plt.imshow(img1)
    #plt.title('Color Image RGB')
    #plt.xticks([])
    #plt.yticks([])
    #plt.show()

    #cap.release()

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