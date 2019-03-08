from socket import *
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(3)
c,addr=s.accept()#接受浏览器连接
print('connect from',addr)
data=c.recv(4096)#浏览器发送请求
print(data.decode())#请求打印前解码
data=open('test.html','rb')
data=data.read()

c.send(data)


c.close()
s.close()