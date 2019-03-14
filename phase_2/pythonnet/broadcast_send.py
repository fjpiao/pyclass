from socket import *
from time import sleep

addr=('localhost',8888)

s=socket(AF_INET,SOCK_DGRAM)

s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

data='-----------'

while True:
    sleep(2)
    s.sendto(data.encode(),addr)

s.close()