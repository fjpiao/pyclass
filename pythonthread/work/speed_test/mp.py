#4.74秒
from multiprocessing import Process
import time
a1=time.time()
def count(x,y):
    c=0
    while c<7000000:
        c+=1
        x+=1
        y+=1

clist=[]
for i in range(10):
    p=Process(target=count,args=(0,0))
    clist.append(i)
    p.start()

for i in clist:
    p.join()
a2=time.time()

print('多进程运行%.2f秒'%(a2-a1))