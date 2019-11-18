from scapy.all import *

conf.verb=0

request = IP(dst='139.59.90.114',ttl=10)/ICMP()
reply = sr1(request,timeout=2)

print(reply.decode())
