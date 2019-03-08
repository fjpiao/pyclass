#5.065478
from multiprocessing import Process
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
plist=[]
for i in range(10):
    p=Process(target=io)
    plist.append(p)
    p.start()
for i in plist:    
    p.join()
a2=time.time()
print('io多进程%f秒'%(a2-a1))
