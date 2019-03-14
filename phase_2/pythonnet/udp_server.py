from socket import *
sockfd=socket(AF_INET,SOCK_DGRAM)

server_addr=('0.0.0.0',8888)
sockfd.bind(server_addr)

while True:
    data,addr=sockfd.recvfrom(1024)
    data=data.decode()
    print('receive from %s:%s'%addr)
    print(data)
    sockfd.sendto(b'got your message',addr)

sockfd.close()