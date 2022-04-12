# telnet 23
# ssh 22
# http 80 - make a connection - request document 
# - retrieve the document - close the connection
#
# https 443
# smtp 25
# imap 143/220/993 mail retrieval
# pop 109/110 mail retrieval
# dns 53
# ftp 21

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org',80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n' .encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()