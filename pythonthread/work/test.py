#计算密集型　x,y传入1　10遍
#多进程　创建10进程
#多线程　创建10线程
def count(x,y):
    c=0
    while c<7000000:
        c+=1
        x+=1
        y+=1

#io秘籍
def write():
    f=open('text','w')
    for i in range (1200000):
        f.write('hello world\n')
    f.close()

def read():
    f=open('test')
    lines=f.readlines()
    f.close()