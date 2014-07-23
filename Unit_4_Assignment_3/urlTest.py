#import urllib.BeautifulSoup.*




import urllib
from BeautifulSoup import *

url = "http://www.dr-chuck.com/page1.htm"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup("a")
for tag in tags:
    print tag.get("href",None)


'''
import urllib2
request = urllib2.Request('http://diveintomark.org/redir/example301.xml')

import openanything, httplib
httplib.HTTPConnection.debuglevel = 1
opener = urllib2.build_opener(openanything.SmartRedirectHandler())
f = opener.open(request)
'''