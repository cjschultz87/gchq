#https://pythonprogramming.net/python-sockets/

import socket
import ssl

#https://stackoverflow.com/questions/41325233/python-ssl-socket-cant-connect-to-self-signed-certificate
context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
context.verify_mode = ssl.CERT_REQUIRED
context.check_hostname = True
context.load_default_certs()

sierra = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM,proto=0)

address = "dictionary.cambridge.org"

ip = socket.gethostbyname(address)

SIERRA = context.wrap_socket(sierra, server_hostname=address)

print "socket " + str(socket.gethostname()) + " active"
print address
print "ip: " + ip

SIERRA.connect((ip,443))

req = b"GET / HTTP/1.1\r\nHost: "+ip+"\r\n\r\n"

SIERRA.send(req.encode())

strRec = ""

tango = 0

while 1 > 0:
    sierraReq = SIERRA.recv(1024)
    if not sierraReq:
        break
        
    strRec += str(sierraReq)
    
    print "receiving " + str(tango)
    
    tango += 1
    
print strRec

sierra.close()