from socket import *

sockfd=socket()#完全取默认值

server_addr=('localhost',9889)
sockfd.connect(server_addr)
# 
f=open('a.png','rb')#任何类型文件都可以转换成二进制
while True:
    data=f.read(1024)#直接读完内存会溢出
    if not data:
        break
    sockfd.send(data)


f.close()
sockfd.close()
