#Author: Kai Zhang
#cite: https://blog.csdn.net/xiao__run/article/details/76342634

import cv2
import urllib2
import numpy as np 
import sys

host = "192.168.1.220:8080"  #remember to revise the ip address

if len(sys.argv)>1:
	host=sys.argv[1]
hoststr='http://' + host + '/?action=stream'
print 'Streaming' + hoststr

print 'Print Esc to quit'

stream=urllib2.urlopen(hoststr)
bytes=''
while True:
	bytes+=stream.read(1024)
	a = bytes.find('\xff\xd8')
	b = bytes.find('\xff\xd9')
	if a!=-1 and b!=1:
		jpg = bytes[a:b+2]
		bytes = bytes[b+2:]
		#flags =1 for color image
		i = cv2.imdecode(np.fromstring(jpg,dtype=np.unit8),flags=1)
		#print i.shape
		cv2.imshow("Kai",i)
		if cv2.waitKey(1)&0xff == ord('q')
			exit(0)