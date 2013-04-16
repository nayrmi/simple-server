import socket

host = ''
port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)

while 1:
	csock, caddr = s.accept()
	cfile = csock.makefile('rw', 0)
	line = cfile.readline().strip()
	cfile.write('HTTP/1.0 200 OK\n\n')
	cfile.write('<html><head><title>Welcome %s!</title></head>' %(str(caddr))) 
	cfile.write('<body><h1>I made a change!<h1>') 
	cfile.write('All the server needs to do is ') 
	cfile.write('to deliver the text to the socket. ') 
	cfile.write('It delivers the HTML code for a link, ') 
	cfile.write('and the web browser converts it. <br><br><br><br>') 
	cfile.write('<font size="7"><center> <a href="http://python.about.com/index.html">Click me!</a> </center></font>') 
	cfile.write('<br><br>The wording of your request was: "%s"' %(line)) 
	cfile.write('</body></html>') 
	cfile.close()
	csock.close()
