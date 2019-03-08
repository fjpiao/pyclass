from socket import *
from select import *
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(5)
rlist=[s]
wlist=[]
xlist=[]
while True:
    rs,ws,xs=select(rlist,wlist,xlist)
    for r in rs:
        if r==s:    
            c,addr=s.accept()
            rlist.append(c)
        else:
            while True:
                data=c.recv(1024)
                if not data:
                    c.close()
                    rlist.remove(c)
                    break
                print(data.decode())
        



