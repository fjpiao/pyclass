'''
http server v1.0
接受浏览器请求
返回固定的相应内容
'''
from socket import *
#处理客户端请求
def handleClient(connfd):
    print('request from:',connfd.getpeername())
    request=connfd.recv(4096)#接受http请求
    
    request_lines=request.splitlines()#讲request按行分割
    for line in request_lines:
        print(line)
    try:
        f=open('est.html','r')
    except IOError:#文件不存在
        response='HTTP/1.1 404 NOT FOUND\r\n'
        response+='\r\n'
        response+='error'
    else:
        response='HTTP/1.1 200 OK\r\n'
        response+='\r\n'
        response+=f.read()
    finally:
        #将结果发送给浏览器
        connfd.send(response.encode())

#创建套接字    
def main():
    sockfd=socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(('0.0.0.0',8888))
    sockfd.listen(3)
    print('listen to the port 8888')
    while True:
        connfd,addr=sockfd.accept()
        handleClient(connfd)#负责具体请求处理 不需要地址　地址信息已经包含在connfd中
        connfd.close()

if __name__=='__main__':
    main()
