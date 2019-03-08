import re

data=open('data.txt','r')
data=data.read()

def d1(data):
    c=r'[A-Z]'
    r=re.findall(c,data)
    return r
def d2(data):
    while True:
        c=r'\d+\.\d*'
        r=re.findall(c,data)
        return r

if __name__=='__main__':
    print(d2(data))