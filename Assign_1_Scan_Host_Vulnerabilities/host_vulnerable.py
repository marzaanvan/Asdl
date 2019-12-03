import socket
import sys

#connect to given ip and return the recieved value as banner
def retBanner(ip,port):
    try:
        s = socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip,port))
        banner = s.recv(1024)
        return banner
    except:
        return 

#check for vulnerability and return 
def checkVulns(banner):
    if 'FreeFloat Ftp Server (Version 1.00)' in banner:
        print('[+] FreeFloat FTP Server is Vulnerable')

    elif '3Com 3CDaemon FTP Server Version 2.0' in banner:
        print('[+] 3CDaemon FTP Server is vulnerable.')

    elif 'Ability Server 2.34' in banner:
        print('[+] Ability FTP Server is vulnerable.')

    elif 'Sami FTP Server 2.0.2' in banner:
        print('[+] Sami FTP Server is vulnerable.')

    else:
        print('[-] FTP Server is not vulnerable.')

    return


#main code starts here
if len(sys.argv) < 2:
    print("Usage: python3 host_vulnerable.py [ IP ]")
    exit()

port_list = [21,22,23,34,80,110,2222,443]
for x in range(100,210):
    ip = '.'.join(sys.argv[1].split('.')[:3]) + '.' + str(x)

    for port in port_list:
        banner = retBanner(ip,port)
        if banner:
            print(' [+] ' + ip + ': ' + banner.decode('ascii'))
            checkVulns(banner.decode())
        break


