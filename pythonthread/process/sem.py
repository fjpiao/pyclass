from multiprocessing import Semaphore,Process
from time import sleep
import os

#创建信号量
sem=Semaphore(3)

def fun():
    print('%d 想执行事件'%os.getpid())
    #想执行事件必须得到信号量资源
    sem.acquire()
    print('%s抢到了一个信号量，可以执行操作'%os.getpid())
    sleep(3)
    print('%d执行完事件再增加信号量'%os.getpid())
    sem.release()

jobs=[]
for i in range(5):
    p=Process(target=fun)
    p.start()

for i in jobs:
    i.join()

print(sem.get_value())