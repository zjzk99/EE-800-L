#!/usr/bin/env python
# encoding=utf-8
 
import time		#导入定时
import urllib2	#导入url
import re		#导入正则
import commands	#导入调用shell命令模块
 
def mjpg_jpg():
	commands.getstatusoutput('/etc/init.d/mjpg-streamer start')	#开启mjpg-streamer进程
	a = commands.getstatusoutput('ps')
	print a
	time.sleep(1)	#延时
	
	req = urllib2.urlopen("http://192.168.1.1:8080/?action=stream")
	buf = req.read(71)		#取出包含jpg长度的信息头
	a = "\d+"			#设置匹配规则取出jpg数据长度
	m = re.findall(a,buf)	#正则取出
	print "jpg0:",m		#打印出来看看
	buf_1 = req.read(27)	#取出mjpeg包含运行时间数据，没用扔掉
	if len(m) > 0:
		jpg_s0 = int(m[0])	#jpg长度转int
	jpg0 = req.read(jpg_s0)	        #取出jpg数据
	l = req.read(3)			#垃圾扔掉
	
	buf = req.read(71)
	a = "\d+"
	m = re.findall(a,buf)
	print "jpg1:", m
	buf_1 = req.read(27)
	if len(m) > 0:
		jpg_s1 = int(m[0])
	jpg1 = req.read(jpg_s1)
	l = req.read(3)
 
	buf = req.read(71)
	a = "\d+"
	m = re.findall(a,buf)
	print "jpg2:",m
	buf_1 = req.read(27)
	if len(m) > 0:
		jpg_s2 = int(m[0])
	jpg2 = req.read(jpg_s2)
	l = req.read(3)
	
	buf = req.read(71)
	a = "\d+"
	m = re.findall(a,buf)
	print "jpg3:",m
	buf_1 = req.read(27)
	if len(m) > 0:
		jpg_s3 = int(m[0])
	jpg3 = req.read(jpg_s3)
	l = req.read(3)
	
	buf = req.read(71)
	a = "\d+"
	m = re.findall(a,buf)
	print "jpg4:",m
	buf_1 = req.read(27)
	if len(m) > 0:
		jpg_s4 = int(m[0])
	jpg4 = req.read(jpg_s4)
	l = req.read(3)
 
#下面部分比列表中哪帧数据最大就用哪张
	jpg_list = [jpg_s0,jpg_s1,jpg_s2,jpg_s3,jpg_s4]
	aa = 0
	for i in jpg_list:
		if i>aa:
			aa = i
	if len(jpg0)==aa:
		jpg = jpg0
	elif len(jpg1)==aa:
		jpg = jpg1
	elif len(jpg2)==aa:
		jpg = jpg2
	elif len(jpg3)==aa:
		jpg = jpg3
	elif len(jpg4)==aa:
		jpg = jpg4
	print aa
	print jpg_s0,jpg_s1,jpg_s2,jpg_s3,jpg_s4	
#上面###########
#下面这部分将jpg写入以时间命名的文件名	
	b = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	c = b+".jpg"
	print c
	fp = open(c,"w")
	fp.write(jpg)
	fp.close()
 
	commands.getstatusoutput('/etc/init.d/mjpg-streamer stop')	#关闭mjpg-streamer进程
	a = commands.getstatusoutput('ps')
	print a
if __name__ == '__main__':
	mjpg_jpg()
#	time.sleep(0.5)		#延时0.5秒，防止占用cpu资源