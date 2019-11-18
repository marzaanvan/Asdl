#Sniffing Packets using Scapy and sending packet data to callback function Filtering with TCP

from scapy.all import *

#Callback Function
def sniffing(pkt):
	pkt.show()

sniff(filter='tcp',prn=sniffing)

