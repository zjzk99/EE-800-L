#!/bin/bash
	ftp -v -n 192.168.1.248 << EOF
    user kai zhangkai
    binary
	hash
	cd /home/pi/rpi
    lcd /home/kai/kevin
    prompt
    mput *
    bye
    EOF