import signal
import os
#处理子进程退出 父进程忽略子进程退出信号
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

pid=os.fork()
if pid<0:
    print('error')
elif pid==0:
    print('child PID:',os.getpid())
else:
    while True:
        pass

