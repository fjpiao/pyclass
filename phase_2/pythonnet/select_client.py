from socket import *

sockfd=socket()#完全取默认值

server_addr=('localhost',8888)
sockfd.connect(server_addr)

while True:
    data=input('=')
    if not data:
        break
    
    
    sockfd.send(data.encode())
    



sockfd.close()
