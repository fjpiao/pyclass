'''
ftp文件服务器

'''
from socket import *
import os,sys
import signal
import time
#全局变量
HOST='0.0.0.0'
PORT=8888
ADDR=(HOST,PORT)
FILE_PATH='/home/tarena/test/pythonthread/work/database/'
class FtpServer(object):
    def __init__(self,connfd):
        self.connfd=connfd

    def do_list(self):
        #获取文件列表
        file_list=os.listdir(FILE_PATH)
        if not file_list:
            self.connfd.send('文件库为空'.encode())
            return
        else:
            self.connfd.send(b'OK')
            time.sleep(0.1)#让客户端充分的时间接受发送的'OK'

        files=''
        for file in file_list:
            if file[0]!='.' and os.path.isfile(FILE_PATH+file):#去除隐藏文件
                files=files + file +','
        #将拼接好的字符串传给客户端
        self.connfd.send(files.encode())
    def do_get(self,filename):
        try:
            fd=open(FILE_PATH+filename,'rb')
        except IOError:
            self.connfd.send('文件不存在'.encode())
            return
        else:
            self.connfd.send(b'OK')
            time.sleep(0.1)
        #发送文件内容
        while True:
            data=fd.read(1024)
            if not data:
                time.sleep(0.1)
                self.connfd.send(b'##')
                break
            self.connfd.send(data)

    def do_put(self,filename):
        if os.path.exists(FILE_PATH+filename):
            self.connfd.send('该文件已存在'.encode())
            return
        fd=open(FILE_PATH+filename,'wb')
        self.connfd.send(b'OK')
        #接受文件
        while True:
            data=self.connfd.recv(1024)
            if data==b'##':
                break
            fd.write(data)
        fd.close()

def do_request(connfd):
    ftp=FtpServer(connfd)

    while True:
        data=connfd.recv(1024).decode()    
        if not data or data[0]=='Q':#当data为空时　data[0]会报错　
            connfd.close()
            return
        elif data[0]=='L':
            ftp.do_list()
        elif data[0]=='G':
            filename=data.split(' ')[-1]
            ftp.do_get(filename)
        elif data[0]=='P':
            filename=data.split(' ')[-1]
            ftp.do_put(filename)

        





#网络搭建
def main():
    #创建套接字
    sockfd=socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(ADDR)
    sockfd.listen(5)
    print('Listen the port 8888....')
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)

    while True:
        try:
            connfd,addr=sockfd.accept()
        except KeyboardInterrupt:
            sys.exit('服务器退出')
        except Exception as e:
            print('Error:',e)
            continue
        print('连接客户端:',addr)

        #创建子进程
        pid=os.fork()
        if pid==0:
            sockfd.close()
            do_request(connfd)
            os._exit()
        else:
            connfd.close()
if __name__=='__main__':
    main()