import socket

s = socket.socket()

host = '127.0.0.1'
port  = 8080

s.bind((host,port))

s.listen(5)

while True:

