#Sniffing the IP packets and printing custom data as required (Source and Destination MAC Address)

from scapy.all import *

def sniffing(pkt):
	print("Source MAC: %s <-----> Dest MAC: %s" %(pkt[Ether].src,pkt[Ether].dst))

sniff(filter='tcp',prn=sniffing)


