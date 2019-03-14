# insert.py
# 插入示例
import pymysql
from db_conf import *

try:
    # 连接数据库
    conn = pymysql.connect(host, user, \
                   passwd, dbname)    
    cursor = conn.cursor()  # 获取游标
    # 执行SQL语句     # 10:40
    sql = '''insert into acct values
      ('62234500000008','Steven', 'C0008',
       1, date(now()), 1, 6666.55)  '''
    cursor.execute(sql)  #执行插入
    conn.commit()  #提交事务
    cursor.close()  #关闭游标
    print("插入成功")
except Exception as e:
    conn.rollback()   #出现异常，回滚事务
    print("数据库操作失败")
    print(e)
finally:
    conn.close()   #关闭连接











