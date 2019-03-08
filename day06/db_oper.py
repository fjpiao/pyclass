# db_oper.py
# 数据库访问层
# 作用：创建从mysql数据库中调取数据的渠道，但不输入具体sql语言
import db_conf
import pymysql

class DBOper:
    def __init__(self): #构造方法
        self.host = db_conf.host
        self.user = db_conf.user
        self.passwd = db_conf.passwd
        self.dbname = db_conf.dbname
        self.db_conn = None  #数据库连接对象

    def open_conn(self): #连接数据库
        try:
            self.db_conn = pymysql.connect(
                self.host, self.user, 
                self.passwd, self.dbname)
        except Exception as e:
            print("数据库连接错误")
            print(e)
        else:
            print("数据库连接成功")

    def close_conn(self):#关闭连接
        try:
            self.db_conn.close()
        except Exception as e:
            print("数据库关闭错误")
            print(e)
        else:
            print("数据库关闭成功")

    # 执行查询, 返回结果集
    #-------参数合法性判断-----------
    def do_query(self, sql): 
        if not sql:  
            print("SQL语句不合法")
            return None 

        if sql == "": 
            print("SQL语句不合法")
            return None 
    #------------执行查询---------------
        try:
            cursor = self.db_conn.cursor()#获取游标
            cursor.execute(sql) #执行sql语句
            result = cursor.fetchall() #获取数据
            cursor.close() #关闭游标
            return result  #返回查询数据集 
        except Exception as e:
            print("查询出错")
            print(e)
            return None

    # 执行增、删、改等变更操作           
    def do_update(self, sql): 
        if not sql:  #参数合法性判断
            print("SQL语句不合法")
            return None 

        if sql == "": #参数合法性判断
            print("SQL语句不合法")
            return None 

        try:
            cursor = self.db_conn.cursor()#获取游标
            result = cursor.execute(sql)#执行SQL语句
            self.db_conn.commit()  #提交事务
            cursor.close()
            return result  #返回受影响的笔数
        except Exception as e:
            print("执行SQL语句出错")
            print(e)
            return None

#测试
if __name__ == "__main__":
    dboper = DBOper()  #实例化数据库操作对象
    dboper.open_conn() #连接数据库
    #查询测试
    # result = dboper.do_query("select * from acct")
    # for x in result:
    #     print(x)

    #修改数据测试
    sql = '''update acct set balance = balance + 100
             where acct_no = '62234500000008'
    '''
    ret = dboper.do_update(sql)
    if not ret:  #返回空对象，出错
        print("执行修改错误")
    else: #非空对象，执行成功
        print("影响笔数:%d" % ret)

    dboper.close_conn()  #关闭数据库连接