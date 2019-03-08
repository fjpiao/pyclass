import os
from time import sleep
pid=os.fork()
if pid<0:
    print('error')
elif pid==0:
    sleep(3)
    print('child %d process exit'%os.getpid())
    os._exit(2)
else:
    while True:
        p,status=os.waitpid(-1,os.WNOHANG)
        if p!=0:
            break
        sleep(1)
        print('做了其他事情')

    while True:
        print('完成父进程‘)
        sleep(2)
        