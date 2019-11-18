#Sniffing the IP packets and printing custom data from packet as required (Source and Destination IP)

from scapy.all import *

def sniffing(pkt):
	print("Source IP: %s <-----> Dest IP: %s" %(pkt[IP].src,pkt[IP].dst))

sniff(filter='IP',prn=sniffing)


