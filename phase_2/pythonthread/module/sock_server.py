#coding:utf-8
'''
使用socketserver模块完成网络并发模型
'''
from socketserver import *

#创建tcp 多进程并发
class Server(ForkingMixIn,TCPServer):
    pass

#具体请求处理类
class Handler(StreamRequestHandler):

    #重写具体处理方法
    def handle(self):
        print('Connect from',self.client_address)
        while True:
            data=self.request.recv(1024)
            if not data:
                break
            print(data.decode())
            self.request.send(b'ok')
    
server_addr=('0.0.0.0',8888)
#创建服务器对象
server=Server(server_addr,Handler)
server.serve_forever()#启动服务

