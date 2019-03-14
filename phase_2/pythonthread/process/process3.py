from multiprocessing import Process
from time import sleep

#带参数的进程函数
def worker(sec):
    for i in range(3):
        sleep(sec)
        print("I'm")
        print("I'm working...")

# p=Process(target=worker,args=(2,'Levi'))
# p=Process(target=worker,kwargs={'name':'Tom','sec':2})
p=Process(target=worker,args=(2,))
p.start()
p.join()
