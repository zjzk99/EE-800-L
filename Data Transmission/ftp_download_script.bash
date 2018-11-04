#!/bin/bash
	ftp -v -n 192.168.1.248<
	user kai zhangkai
    binary
    cd /home/kai/kevin
    lcd /home/pi/rpi
    prompt
    mget *
    close
    byeEOF
	