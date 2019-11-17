import socket

s = socket.socket()

host = '127.0.0.1'
port  = 78695

s.bind((host,port))

s.listen(5)

#while True:
conn, addr = s.accept()
print("New Connection Recived from " + str(addr))

msg = conn.recv(1024).decode("ascii")
print(type(msg))
print("Message Recieved := " + str(msg))


