import pymysql
from db_conf import *

try:
#连接数据库
    conn=pymysql.connect(host,user,passwd,dbname)
#获取游标-终端输入
    cursor=conn.cursor()
#执行SQL语句
    sql=''''''
    cursor.execute(sql)#执行插入 自动开启事务
    conn.commit()#提交
    print('操作成功')

except Exception as e:#e=错误信息
    conn.rollback()#出现异常事务回滚
    print('数据库操作失败')
    print(e)
finally:
    conn.close()#关闭连接