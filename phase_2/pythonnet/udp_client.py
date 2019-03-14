from socket import *
sockfd=socket(AF_INET,SOCK_DGRAM)
addr=('localhost',8888)
while True:
    data=input('=')
    if not data:
        break
    data=data.encode()
    sockfd.sendto(data,addr)
    data,addr=sockfd.recvfrom(1024)
    data=data.decode()
    print('receive from %s:%s'%addr,data)
sockfd.close()