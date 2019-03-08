import gevent
import time
def foo():
    print('Running foo')
    gevent.sleep(3)
    print('Foo again')

def bar():
    print('Running bar')
    gevent.sleep(2)
    print('Bar again')

f=gevent.spawn(foo)
b=gevent.spawn(bar)

gevent.joinall([f,b])