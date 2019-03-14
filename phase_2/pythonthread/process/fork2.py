import os
from time import sleep 
print('...')#只运行一次
a=1#但赋值会留给子进程　父进程的空间会拷贝到子进程空间中
pid=os.fork()
if pid<0:
    print('create process failed')
elif pid==0:
    print('child process')
    print('a=%d'%a)
else:
    print('parent process')