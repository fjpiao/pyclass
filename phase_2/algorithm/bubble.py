
def test(value):
    for i in range(len(value)-1):

        flag = False

        for j in range(len(value)-i-1):
            #从低到高
            if value[j]>value[j+1]:
                value[j],value[j+1]=value[j+1],value[j]

                flag = True
    

#如未发生数据交换，则说明后续数据均有序

if flag==False:

if __name__=='__main__':
    L=[1,2,3,4,5]
    test(L)