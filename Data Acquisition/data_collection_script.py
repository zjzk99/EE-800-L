# Author: Kai Zhang
# Stevens Institute of Technology

# import camera
import camera_script
import cv2
import time # create a file name with the current data & time
import sys
global timer
import threading

def judge():
	print("Take 10 pictures in 10s")

if __name__ == '__main__':
	#data.py executed as script
	judge()
	#run the camera.py
	# num=0
	camera_script.pic_shot_run()
 #    cap=cv2.VideoCapture(0)
 #    timer=threading.Timer(1, main)
 #    timer.start()
 #    camera.main()-