#6.114947
from threading import Thread
import time


def write():
    f=open('text.txt','w')
    for i in range (1200000):
        f.write('hello world\n')
    f.close()

def read():
    f=open('text.txt','r')
    lines=f.readlines()
    f.close()
def io():
    write()
    read()
    write()
a1=time.time()
tlist=[]
for i in range(10):
    t=Thread(target=io)
    tlist.append(t)
    t.start()
for i in tlist:    
    t.join()
a2=time.time()
print('io多线程%f秒'%(a2-a1))