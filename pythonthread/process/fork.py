#fork函数返回两次 实现两进程同时运行
#创建两个进程
import os
from time import sleep
pid=os.fork()
#创建了新的进程——>子进程　
#子进程从fork函数返回值给pid开始
#父子进程互相抢占时间片　先抢先运行　目前程序中父进程概率大　但运行是并发(或并行)运行


if pid<0:
    print('create process failed')
elif pid==0:
    sleep(4)
    print('the new process1')

else:
    sleep(2)
    print('the old process')

print('fork test over')