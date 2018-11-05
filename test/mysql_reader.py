'''
Created on 2017年11月11日

@author: Administrator
'''
import pymysql.cursors

connection = pymysql.connect(host = "localhost",
                             user = "root",
                             password = "123456",
                             db = "spider",
                             charset = "utf8mb4"
                            )
try:
  #获取会话指针
  with connection.cursor() as cursor:
        #创建sql
    sql = "select `url`,`title` from `baike` where `id` is not null"
    count = cursor.execute(sql)
    print(count)
    a =  cursor.fetchone()
    print(a)
    cursor.fetchmany(size = 1)
    all = cursor.fetchall()
    print (all)
    connection.commit()
finally:
  connection.close()