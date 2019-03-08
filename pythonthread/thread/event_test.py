from threading import Event

#创建事件对象
e=Event()

e.set()#设置e

e.clear()#清除set状态
print(e.is_set())
e.wait(3)

print('88888888')