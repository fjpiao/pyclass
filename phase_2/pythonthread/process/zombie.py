
import os
from time import sleep

pid=os.fork()

if pid==0:
    print('child PID:',os.getpid())
    os.exit(0)
else:
    print('parent process,')
        while 1:
            pass