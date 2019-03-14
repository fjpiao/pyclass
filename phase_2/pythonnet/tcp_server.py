from socket import *

sockfd=socket(AF_INET,SOCK_STREAM)
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(('0.0.0.0',9889))
sockfd.listen(5)

print('waiting for connect')
connfd,addr=sockfd.accept()

    
print('connect from',addr)
nf=open('bbb.png','wb')

while True:
    data=connfd.recv(1024)
    nf.write(data)
    if not data:#客户端断开时发送空值
        break
nf.close()
connfd.close()
sockfd.close()
    