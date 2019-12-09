from scapy.all import *
import sys

if len(sys.argv) < 2:
    print('Usage: python3 ipspoof.py <custom_src_ip>')
    exit(0)

print(sys.argv)

#Preparing  Spoofed packet with custom source IP 
pkt = IP(src=sys.argv[1],dst='159.24.67.32')/TCP(sport=4000,dport=80)

for port in range(1000,10000):

    #Changing source port address in every iteration
    pkt[TCP].sport = port   

    print(port)

    #sending packet on the network
    send(pkt)
