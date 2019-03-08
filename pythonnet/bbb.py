from socket import *
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

s.connect(('0.0.0.0',8888))
while True:
    data=input('=')
    data=data.encode()
    s.send(data)
    if not data:
        s.close
        break