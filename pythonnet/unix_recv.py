from socket import *
import os
#确定套接字文件路径
sock_file='./sock'

#删除之前的sock文件
if os.path.exists(sock_file):
    os.remove(sock_file)
#创建本地套接字
sockfd=socket(AF_UNIX,SOCK_STREAM)

#创建并绑定套接字文件
sockfd.bind(sock_file)

#监听　连接
sockfd.listen(3)
while True:
    c,addr=sockfd.accept()
    while True:
        data=c.recv(1024)
        if not data:
            break
        print(data.decode())
    c.close()
sockfd.close()