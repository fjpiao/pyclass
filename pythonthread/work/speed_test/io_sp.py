#6.389355
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

a1=time.time()
for i in range(10):
    write()
    read()


a2=time.time()
print('io单线程%f秒'%(a2-a1))