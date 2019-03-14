#db_oper.py
#数据库访问类
import pymysql
from db_conf import *
class Dboper:
    def __init__(self):#构造
        self.host=host
        self.user=user
        self.passwd=passwd
        self.dbname=dbname
        self.conn=None#定义空对象
        self.connn=None
        self.open_conn()

    def open_conn(self):#连接数据库
        try:
            a=self.conn=pymysql.connect(
                self.host,self.user,
                self.passwd,self.dbname)
            
            
            
        except Exception as e:
            print('连接失败')
            print(e)
        else:
            print('连接成功')
            print(a)
    def close_conn(self):#关闭连接
        try:
            self.connn.close()
            
        except Exception as e:
            print('关闭失败')
            print(e)
        else:
            print('关闭成功')

    def do_query(self,sql):#执行查询　返回结果集
        if not sql:
            print('语句不合法')
            return None
        try:
            cursor=self.conn.cursor()#局部化
            cursor.execute(sql)
            result=cursor.fetchall()
            
            print('查询成功')
            return result
        except Exception as e:
            print('查询失败')
            print(e)
        finally:
            cursor.close()
    def do_update(self,sql):#执行修改 
        if not sql:
            print('语句不合法')
            return None
        try:
            cursor=self.conn.cursor()#全局变量局部化
            result=cursor.execute(sql)
            self.conn.commit()
            cursor.close()#失败概率低 可以不用finally
            
        except Exception as e:
            self.conn.rollback()
            print('修改失败')
            print(e)
        else:
            print('修改成功')
            return result#返回受影响的笔数
if __name__=='__main__':
    dboper=Dboper()  

    ret=dboper.do_update('insert into aa values(now(),null,2,11)')
    if not ret:#返回空对象时出错
        print('修改无效')
    else:
        print('影响笔数%d' %ret)
    print()
    dboper.close_conn()
