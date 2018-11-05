'''
Created on 2017年11月11日

@author: Administrator
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pymysql

resp = urlopen("https://en.wikipedia.org/wiki/Main_Page").read().decode("utf-8")

soup = BeautifulSoup(resp, "html.parser")

print(soup)

listUrls = soup.findAll("a", href=re.compile("^https"))
print(listUrls)
for url in listUrls:
  if not re.search("\.(jpg|JPG)$", url["href"]):
    #url.string()只能获取一个，下面的是可以获取所有的内容
    print(url.get_text(),"<!------!>",url["href"])
    #获取数据库连接
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
        sql = "insert into `baike`(`title`,`url`) values(%s,%s)"
        
        cursor.execute(sql,(url.get_text(),url["href"]))
        
        connection.commit()
        
    finally:
      connection.close()


