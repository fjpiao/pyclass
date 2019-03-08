import re
import sys

port = sys.argv[1]

f = open('1.txt')

#找到端口所在的对应段落
while True:
    data=''
    for line in f:
        if line !='\n':
            data+=line
        else:
            break
    if not data:
        break
    
#通过首单词比对是否为目标段
    try:
        PORT=re.match(r'\S+',data).group()
    except Exception:
        continue
    if port ==PORT:
        # pattern=r'[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}'
        pattern=r'\d{1,3}'
        address=re.search(pattern,data).group()
        print(address)
        break
f.close()    