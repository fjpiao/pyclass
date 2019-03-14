from socket import *
sock_file='./sock'
sockfd=socket(AF_UNIX,SOCK_STREAM)
sockfd.connect(sock_file)
while True:
    data=input('=')
    if not data:
        break
    sockfd.send(data.encode())
sockfd.close()
