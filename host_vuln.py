import socket


for port in range(1,65534):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect(('139.59.90.114',port))
        banner = s.recv(1024)
        print(banner)

    except:
        print("Error in connection")

