from multiprocessing import process
import time

#自定义进程类
class ClockProcess(Process):
    def __init__(self,value):
        self.value=value
        super().__init__()
#重写run
    def run(self):
        for i in range(5):
            print('The time is %s'%time.ctime())
            time.sleep(self.value)
#创建进程对象
p＝ClockProcess(2)
#启动新的进程
p.start()
p.join()