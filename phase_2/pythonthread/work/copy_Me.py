#作业　讲图片分割一半
from multiprocessing import Process
import os

filename='./a.png'
#获取文件大小
size=os.path.getsize(filename)
f=open(filename,'rb')
#复制上半部分
def top():
    # f=open(filename,'rb')　#父进程创建的对象可以在子进程使用
    n=size//2
    fw=open('half_top.jpg','wb')
    while True:
        if n<1024:
            data=f.read(n)
            fw.write(data)
            break
        data=f.read(1024)
        fw.write(data)
        n-=1024

#复制下半部分 由于没有图片起始标示　看不到下半部
def boot():
    f=open(filename,'rb')
    fw=open('half_bottom.jpg','wb')
    f.seek(size//2,0)#读写位置向后移动size//2个字节

    while True:
        data=f.read(1024)
        if not data:
            break
        fw.write(data)
    f.close()
    fw.close()
f=open(filename,'rb')
t=Process(target=top)
b=Process(target=boot)
t.start()
b.start()
t.join()
b.join()