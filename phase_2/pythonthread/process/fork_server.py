from socket import *
import os,sys
import signal

#客户端处理函数
def client_handle(c):
    print('客户端:',c.getpeername())
    while True:
        data=c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'message received')
    c.close()

#创建监听套接字
host='0.0.0.0'
port=8888
addr=('0.0.0.0',8888)

s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(addr)
s.listen(5)

#处理僵尸进程
signal.signal(signal.SIGCHLD,signal.SIG_IGN)
#循环等待客户端连接
while True:
    try:
        c,addr=s.accept()
    except KeyboardInterrupt:
        sys.exit('服务器退出')
    except Exception as e:
        print('Error:',e)
        continue
    #创建子进程处理客户端请求
    pid=os.fork()
#父进程s,c 子进程c
    #子进程
    if pid==0:
        s.close()
        client_handle(c)#处理客户端请求
        os._exit(0)
    else:#父进程什么都不做　创建进程失败时循环回去接受新的连接
        c.close()
        print(pid)
        pass
        
        