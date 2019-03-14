from socket import *
import struct

s=socket(AF_INET,SOCK_DGRAM)
s.bind(('0.0.0.0',8888))

#确定数据结构 收发两端需要格式一致
st=struct.Struct('i16sf')
while True:
    data,addr=s.recvfrom(1024)
    #解析数据
    data=st.unpack(data)
    print(data)
s.close()