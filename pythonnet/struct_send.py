from socket import *
import struct
ADDR=('127.0.0.1',8888)
s=socket(AF_INET,SOCK_DGRAM)

while True:
    id=int(input('id='))
    name=input('name=')
    height=float(input('height='))
    len=len(name)

    fmt='i16sf'
    data=struct.pack(fmt,id,name.encode(),height)
    s.sendto(data,ADDR)

s.close()

