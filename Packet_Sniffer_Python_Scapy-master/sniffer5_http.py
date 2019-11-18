#Sniffing TCP data of Port 80 and displaying SRC and DST IP alson with HTTP Payload

from scapy.all import *

def sniffing(pkt):
	print("Source IP: {} <--HTTP--> Dest IP: {} Dest Port: {}  Payload:\n{}\n\n".format(pkt[IP].src,pkt[IP].dst,pkt[TCP].dport,pkt[TCP].payload))

sniff(filter='tcp port 80',prn=sniffing)


