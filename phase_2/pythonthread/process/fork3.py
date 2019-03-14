import os
from time import sleep 
print('...')#只运行一次
a=1
pid=os.fork()
if pid<0:
    print('create process failed')
elif pid==0:
    print('child process')
    print('a=%d'%a)
    a=10000
else:
    sleep(1)#让子进程先执行
    print('parent process')
    print('a:'a)
print(a)