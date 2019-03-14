#coding=utf-8
'''
HTTP Server v2.0
*多线程并发
*基本的request解析
*能够反馈基本数据
*使用类封装
'''
from socket import *
from threading import Thread
import sys
#封装具体的类作为HTTP server功能模块
class HTTPServer(object):
    def __init__(self,server_addr,static_dir):
        #添加对象属性
        self.server_address=server_addr
        self.static_dir=static_dir
        self.create_socket()
        self.bind()
    def create_socket(self)
        self.sockfd=socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

    def bind(self):
        self.sockfd.bind(self.server_address)
        self.ip=self.server_address[0]
        self.port=self.server_address[1]


    #启动服务
    def serve_forever(self):
        self.sockfd.listen(5)
        print('Listen the port %d'%self.port)
        while True:
            try:
                connfd,addr=self.sockfd.accept()
            except KeyboardInterrupt:
                self.sockfd.close()
                sys.exit('退出服务器')
            except Exception as e:
                print('Error:',e)
                continue
            #创建多线程处理请求
            clientThread=Thread(target=self.handle,\
                args=(connfd,))
            clientThread.setDaemon(True)
            clientThread.start()

    #具体处理http请求
    def handle(self,connfd):
        #接受HTTP请求
        request=connfd.recv(4096)
        #防止浏览器异常断开
        if not request:
            connfd.close()
            return
        #请求解析
        requestHeaders=request.splitlines()
        print(connfd.getpeername(),':',requestHeaders[0])
        #获取请求内容
        getRequest=str(requestHeaders[0]).split(' ')[1]

        if getRequest=='/' or getRequest[-5:]=='.html':
            self.get_html(connfd,getRequest)
        else:
            self.get_data(connfd.getRequest)
        connfd.close()

    def get_html(self,connfd,getRequest):
        if getRequest=='/':
            filename=self.static_dir+'/index.html'
        else:
            filename=self.static_dir+getRequest
        try:
            f=open(filename)
        except IOError:
            #没有找到网页
            responseHeaders='HTTP/1.1 404 Not Found\r\n'
            responseHeaders+='\r\n'
            responseBody='Sorry Not found the page'
        else:
            #返回网页内容
            responseHeaders='HTTP/1.1 200 OK\r\n'
            responseHeaders+='\r\n'
            responseBody=f.read()
        finally:
            response=responseHeaders+responseBody
            connfd.send(response.encode())
    
    def get_data(self,connfd,getRequest):
        responseHeaders='HTTP/1.1 200 OK\r\n'
        responseHeaders+='\r\n'
        responseBody='<p>waiting httpserver v3.0</p>'
        response=responseHeaders+responseBody
        connfd.send(response.encode())



if __name__=='__main__':
    #使用者自己设定address
    server_addr=('0.0.0.0',8000)
    #用户提供存放网页的目录
    static_dir='./static'

    #创建服务器对象
    httpd=HTTPServer(server_addr,static_dir)
    #启动服务
    httpd.serve_forever()

