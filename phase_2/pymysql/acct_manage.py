#acct_manage.py
#账户管理类(业务逻辑层)
#实现账户新增，修改，查询，删除等逻辑处理
#将数据库列表中数据实例化
from db_oper import *
class Acct:#账户类　仅用于数据传输
    def __init__(self,acct_no,acct_name,acct_type,balance):
        self.acct.no=acct_no
        self.acct.name=acct_name
        self.acct.type=acct_type
        self.balance=balance
    def __str__(self):
        ret='%s,%s,%d,%.2f'%
            (self.acct_no,
            self.acct.name,
            self.acct.type,
            self.balance)
        return ret

class AcctManage:
    def __init__(self,db_oper):
        self.db_oper=db_oper#数据访问对象
    #查询所有账户信息
    def query_all_acct(self):
        accts=[] #返回的Acct对象列表,可能有多个对象
        #写所需要的SQL语句
        sql='select * from aa'
        #执行查询
        result=self.db_oper.do_query(sql)
        if not result:
            print('查询结果为空')
            return None
        #返回结果:实例化一个Acct返回对象的列表
        for r in result:
            acct_no=r[0]
            acct_name=r[1]
            acct_type=r[3]
            balance=r[6]
            accts.append(Acct(acct_no,acct_name,
                            acct_type,balance))
        return accts　#返回对象列表
            
D=Dboper()
D.
