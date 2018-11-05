#http://www.thsrc.com.tw/tw/TimeTable/SearchResult
from urllib.request import urlopen
from urllib.request import Request
from urllib import parse

req = Request("http://www.thsrc.com.tw/tw/TimeTable/SearchResult")

postData = parse.urlencode([("StartStation", "977abb69-413a-4ccf-a109-0272c24fd490"),
                            ("EndStation", "e6e26e66-7dc1-458f-b2f3-71ce65fdc95f"),
                            ("SearchDate", "2017/11/10"),
                            ("SearchTime", "16:09"),
                            ("SearchWay", "DepartureInMandarin")
                             ])

req.add_header("Origin", "http://www.thsrc.com.tw")
req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
resp = urlopen(req, data=postData.encode("utf-8"))
print(resp.read().decode("utf-8"))
