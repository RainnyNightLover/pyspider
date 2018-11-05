'''
Created on 20171110

@author: Administrator
'''
import urllib2

class HtmlDownloader(object):
    
    def download(self,url):
        if url is None:
          return None
        fails = 0
        #add this try code to create the blocking problem when the net is unstable
        while True:
          try:
            if fails >=5:
              break
            response = urllib2.urlopen(url,None,5)
            if response.getcode() !=200:
              return None
            return response.read()
          except:
            fails +=1
            print 'the net was unstable and we are tying again:',fails
          else:
            break
    
    



