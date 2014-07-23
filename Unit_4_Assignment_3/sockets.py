import socket

mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySock.connect(("www.py4inf.com",80))
#mySock.send("GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n")
#mySock.send("GET http://www.py4inf.com/code/urljpeg.py HTTP/1.0\n\n")
mySock.send("GET http://www.py4inf.com/code/BeautifulSoup.py HTTP/1.0\n\n")


#data = mySock.recv(512)
#print len(data)
#print data

while True:
    data = mySock.recv(512)
    if len(data) < 1:
        break
    print data

'''
while len(data) > 1:
    print data

mySock.close()
'''
