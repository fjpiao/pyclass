from threading import Thread,Lock

a=b=0#全局变量两个线程都读写

lock=Lock()#锁对象


def value():
    while Ture:
        lock.acquire()#加锁　另一个线程也要加锁
        if a !=b:
            print('a=%d,b=%d'%(a,b))
        lock.release()
t=Thread(target=value)
t.start()
while True:
    with lock:
        a+=1
        b+=1

t.join()            