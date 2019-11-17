import socket

s = socket.socket()

s.connect(('127.0.0.1',8080))
s.send("kaisan Haal Ba Ho, Marde !".encode())

s.close()

