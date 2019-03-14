import os
from time import sleep

pid=os.fork()

if pid<0:
    print('error')
elif pid==0:
    
    print('child PID:',os.getpid())
    print('get parent pid:',os.getppid())
else:
    print('parent PID:',os.getpid())
    print('get child pid:',pid)
