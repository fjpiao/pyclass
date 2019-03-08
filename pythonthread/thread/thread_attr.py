import threading
from time import sleep
import os



#线程函数
def music():
    print('播放学猫叫',os.getpid())

#创建线程对象
t=threading.Thread(target=music,name='tedu')
t.start()
#线程名称
t.setName('t')
print('')
#主线程运行任务
for i in range(3):
    sleep(2)
    print('燃烧',os.getpid())
print('alive:',t.is_alive())
t.join() 