# update.py
# 修改示例
import pymysql
from db_conf import *

try:
    # 连接数据库
    conn = pymysql.connect(host, user, \
                   passwd, dbname)    
    cursor = conn.cursor()  # 获取游标
    # 执行SQL语句   
    sql = '''update acct 
        set balance = balance + 100
        where acct_no = '62234500000008'
    '''
    cursor.execute(sql)  #执行插入
    conn.commit()  #提交事务
    cursor.close()  #关闭游标
    print("修改成功，影响笔数:%d" % cursor.rowcount)
except Exception as e:
    conn.rollback()   #出现异常，回滚事务
    print("数据库操作失败")
    print(e)
finally:
    conn.close()   #关闭连接











