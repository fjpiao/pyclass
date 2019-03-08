#孤儿进程的父进程与原进程不同　会被系统进程收养
#固有进程　在操作系统
import os
from time import sleep

pid=os.fork()

if pid<0:
    print('error')
elif pid==0:
    sleep(1)
    print('child PID:',os.getpid())
    print('get parent pid:',os.getppid())
else:
    
    print('parent PID:',os.getpid())
    print('get child pid:',pid)
