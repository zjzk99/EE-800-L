#SFTP_SERVER="192.168.1.248"
#SFTP_USER="kai"
#SFTP_PWD="zhangkai"

#lftp sftp://$SFTP_USER:SFTP_PWD@$SFTP_SERVER -e 'mirror -r /home/kai/kevin/ ~\a; bye'

SFTP_SERVER="192.168.1.220"
SFTP_USER="pi"
SFTP_PWD="a2358686B"

lftp sftp://$SFTP_USER:SFTP_PWD@$SFTP_SERVER -e 'mirror -r /home/pi/rpi/ ~/EE-800; bye'
