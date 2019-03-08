from multiprocessing import Pool
import time

def fun(n):
    time.sleep(1)
    print(n)
    return 

pool=Pool()
#使用map将事件放入进程池
r=pool.map(fun,['i','e','e'])
pool.close()
pool.join()

print('结果:')