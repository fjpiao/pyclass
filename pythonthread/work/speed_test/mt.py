#8.26
from threading import Thread
import time
a1=time.time()
def count(x,y):
    c=0
    while c<7000000:
        c+=1
        x+=1
        y+=1

tlist=[]
for i in range(10):
    t=Thread(target=count,args=(0,0))
    tlist.append(i)
    t.start()

for i in tlist:
    t.join()
a2=time.time()

print('多线程运行%.2f秒'%(a2-a1))
