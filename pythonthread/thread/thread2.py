from threading import Thread
from time import sleep

#含有参数的线程函数
def fun(sec,name):
    print('线程函数传参')
    sleep(sec)
    print(name,'ok')
threads=[]
for i in range(5):
    t=Thread(target=fun,args=(2,),kwargs={'name':'T%d'%i})
    threads.append(t)
    t.start()
for i in threads:
    t.join()
