#Example using scapy same as interactive mode of scapy
from scapy.all import *

pkts = sniff(filter='tcp',count = 10)

for i in range(10):
	pkts[i].show()
