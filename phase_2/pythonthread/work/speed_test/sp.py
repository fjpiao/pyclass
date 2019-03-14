#8.14秒
import time 
a1=time.time()
def count(x,y):
    c=0
    while c<7000000:
        c+=1
        x+=1
        y+=1
for i in range(10):
    count(0,0)
a2=time.time()
print('单线程耗时%.2f秒'%(a2-a1))