import os,time
pid=os.fork()
signal.signal(signal.SIGCHLD,signal.SIG_IGN)
a=[]
if pid==0:
    time.sleep(1)
    a.append(0)
    print(a)
    

else:
    
    a.append(1)
    print(a)