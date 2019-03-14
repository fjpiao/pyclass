import socket

sockfd=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sockfd.bind(('0.0.0.0',9889))
sockfd.listen(5)
while True:
    
    print('waiting for connect')
    try:
        connfd,addr=sockfd.accept()
    except KeyboardInterrupt:
        print('server exit')
        break
    print('connect from',addr)
    while True:
        data=connfd.recv(1024)
        if not data:
            connfd.close()
            break
        data=data.decode()
        print('Receive message:',data)
     
        n=connfd.send(b'received your message!')
        
        print('Send %d bytes' %n)
sockfd.close()
        


