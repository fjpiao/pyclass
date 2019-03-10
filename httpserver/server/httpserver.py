#!/usr/bin/env python3
#coding=utf-8

'''
AID httpserver v3.0
'''

from socket import *
import sys
from threading import Thread
import json

#导入配置信息
from config import *

#向frame发送请求
def connect_frame(**env):
    s=socket()
    try:
        s.connect(frame_address)
    except Exception as e:
        print(e)
        return
    #将请求发送给frame
    s.send(json.dumps(env).encode())
    data=s.recv(409600).decode()#不是很合理
    return data

#封装httpserver基本功能
class HTTPServer(object):
    def __init__(self,address):
        self.address=address
        self.create_socket()
        self.bind(address)

    #创建套接字
    def create_socket(self):
        self.sockfd=socket()
        self.sockfd.setsockopt(\
            SOL_SOCKET,SO_REUSEADDR,DEBUG)
    
    def bind(self,address):
        self.ip=address[0]
        self.port=address[1]
        self.sockfd.bind(address)

    #启动服务
    def serve_forever(self):
        self.sockfd.listen(10)
        print('Listen the port %d...'%self.port)
        while True:
            try:
                connfd,addr=self.sockfd.accept()
                print('Connect from',addr)
            except KeyboardInterrupt:
                self.sockfd.close()
                sys.exit('退出httpserver服务')
            except Exception as e:
                print(e)
                continue
            client=Thread(target=self.handle,\
                args=(connfd,))
            client.setDaemon(True)
            client.start()

    #处理浏览器的http请求
    def handle(self,connfd):
        request=connfd.recv(4096)
        #处理客户端断开
        if not request:
            connfd.close()
            return
        request_lines=request.splitlines()
        #获取请求行
        request_line=request_lines[0].decode('utf-8')
        print('请求:',request_line)

        #获取请求方法和请求内容
        tmp=request_line.split(' ')
        method=tmp[0]
        path_info=tmp[1]

        data=connect_frame(method=method,\
            path_info=path_info)

        self.response(connfd,data)
    #处理返回的数据内容
    def response(self,connfd,data):
        
        
        #根据情况组织响应
        if data!='404':
            response_headlers='HTTP/1.1 200 OK\r\n'
        else:
            response_headlers='HTTP/1.1 404 Not Found\n'

        response_headlers+='\r\n'
        response_body=data
        response=response_headlers+response_body
        connfd.send(response.encode())
        connfd.close()

httpd=HTTPServer(ADDR)
httpd.serve_forever()#启动服务程序