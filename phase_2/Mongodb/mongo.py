from pymongo import MongoClient

conn=MongoClient('localhost',27017)

db=conn.stu


myset=db.class0

# #数据操作
# myset.insert_one({'name':'张铁林','King':'乾隆'})
myset.insert_many([{'name':'张国立','King':'康熙'},{'name':'陈道明','King':'康熙'}])


conn.close()