#-*-coding:utf-8 -*-
from urllib import request
#visit simple
resp = request.urlopen("http://www.baidu.com")
print(resp.read().decode("utf-8"))

#visit as an exploer
req = request.Request("http://www.baidu.com")
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
resp = request.urlopen(req)
print(resp.read().decode("utf-8"))

