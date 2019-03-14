from socket import *
from select import *

#创建要关注的IO
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(5)

#创建poll对象
p=poll()

#建立查找字典 fileno-
fdmap={s.fileno():s}

#注册IO
p.register(s,POLLIN|POLLERR)

#循环监控
while True:
    events=p.poll()#阻塞
    #遍历列表，处理IO
    for fd,event in events:
        if fd==s.fileno():
            c,addr=fdmap[fd].accept()
            print('connect from',addr)
            #添加新的注册IO
            p.register(c,POLLIN|POLLHUP)
            fdmap[c.fileno()]=c
        elif event & POLLHUP:#判断是否断连
            print('客户端退出')
            p.unregister(fd)#取消关注
            fdmap[fd].close()
            del fdmap[fd]
        elif event & POLLIN:#(按位与)
            data=fdmap[fd].recv(1024)
            print('receive:',data.decode())
            fdmap[fd].send(b'receive your msg')
            


