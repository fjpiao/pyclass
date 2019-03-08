from socket import *
s=socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)#允许发送广播

s.bind(('0.0.0.0',8888))

while True:
    try:
        data,addr=s.recvfrom(1024)
        data=data.decode()
        print('receive from',addr)
        print(data)
    except KeyboardInterrupt:
        break
        print()
    except Exception as e:
        print(e)
s.close()