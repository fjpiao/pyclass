from socket import *
from select import select
from sys import stdin
from time import ctime#当前时间

#创建套接字作为关注的IO
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(5)
#日志文件
f=open('print1.txt','a')#之前文件不删，接着往下写


#添加到关注列表
rlist=[s,stdin]#stdin标准输入
wlist=[]
xlist=[]

while True:
#监控关注的IO
    rs,ws,xs=select(rlist,wlist,xlist)
    
#遍历返回值列表，确定就绪的IO
    for r in rs:
        #s就绪　有客户端请求连接
        if r is s:
            c,addr=s.accept()
            print('connect from',addr)
            rlist.append(c)
        #表示某个客户端发消息则c就绪
        
        if r is stdin:
            data=stdin.readline()


            f.write('%s %s\n'%(ctime(),data))
            f.flush()#刷新文件缓冲 将缓冲数据写入磁盘
        else:
            data=c.recv(1024)
            if not data:
                rlist.remove(c)
                c.close()
                continue
            f.write('%s %s\n'%(ctime(),data.decode()))
            f.flush()
            
            
            
    for w in ws:
        pass
        
    for x in xs:
        pass
    
