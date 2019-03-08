# acct_manage_ui.py (User Interface层)
# 用户接口层　

from db_oper import *
from acct_manage import *
if __name__ == "__main__":
    db_oper = DBOper()  #实例化数据访问对象
    db_oper.open_conn() #打开连接    
    am = AcctManage(db_oper) #实例化账户管理对象
    # 根据用户输入，进行不同操作
    menu = '''
    ---------- 请选取要执行的操作 ----------
      1 - 查询所有
      2 - 根据账户查询     '''
    print(menu)
    oper = input("请选取要执行的操作:")    
    if oper == "1": #查询所有账户，并返回对象列表
        accts = am.query_all_acct()
        for acct in accts: # 打印查询结果
            print(acct)
    elif oper == "2": #根据账户查询，返回一个Acct对象
        acct_no = input("请输入要查询的帐号:")
        acct = am.query_by_id(acct_no) #查询
        print(acct)  #打印查询结果
    else:
        print("选取的操作暂不支持")