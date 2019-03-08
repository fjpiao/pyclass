# acct_manage.py
# 账户管理类(业务逻辑层)　数据管理层
# 实现账户新增、修改、查询、删除等逻辑处理
# 利用数据库访问类程序　对数据输出进行管理　需输入sql语句
from db_oper import *
#账户类，仅用于数据传输
class Acct: 
    def __init__(self, acct_no, acct_name,
                 acct_type, balance):
        self.acct_no = acct_no
        self.acct_name = acct_name
        self.acct_type = acct_type
        self.balance = balance
    def __str__(self):
        ret = "账号:%s,户名:%s,类型:%d,余额:%.2f" % \
            (self.acct_no, self.acct_name,
            self.acct_type, self.balance)
        return ret

class AcctManage: #账户管理类
    def __init__(self, db_oper):
        self.db_oper = db_oper #数据访问对象

    #查询所有账户信息
    def query_all_acct(self):
        accts = []   #返回的Acct对象列表，可能有多个对象
        # 拼装所需要的SQL
        sql = "select * from acct"
        # 执行查询
        result = self.db_oper.do_query(sql)#输出列表
        if not result:
            print("查询结果为空")
            return None
        # 返回结果：实例化一个Acct对象列表返回
        for r in result:  #遍历数据集
            acct_no = r[0] #帐号
            acct_name = r[1] #户名
            acct_type = int(r[3]) #类型
            balance = r[6]  #余额
            accts.append(Acct(acct_no, acct_name,
                              acct_type,balance))
        return accts  #返回对象列表

    #根据账户查询，最多返回一个Acct对象
    def query_by_id(self, acct_no):
        sql = '''select * from acct 
                 where acct_no = '%s' ''' % acct_no
        result = self.db_oper.do_query(sql)#执行查询
        if not result:
            print("查询返回空对象")
            return None
        # 提取查询结果，实例化一个Acct对象返回
        r = result[0]  #取得第一行数据
        acct_no = r[0] #账号
        acct_name = r[1] #户名
        acct_type = int(r[3]) #类型
        balance = r[6]  #余额
        return Acct(acct_no,acct_name,acct_type,balance)
