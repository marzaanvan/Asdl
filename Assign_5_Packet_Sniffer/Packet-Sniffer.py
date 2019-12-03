'''
Author:- Prem Kumar

Assignment No.- 03 : Packet Sniffing using scapy 
'''

from scapy.all import *

#Callback function to filter TCP Packets
def sniff_TCP(pkt):
    pkt.show()

#Callback function to print src and dest IP addresses
def sniff_IP(pkt):
    print("Source IP: %s <-----> Dest IP: %s" %(pkt[IP].src,pkt[IP].dst))

#Callback function to  Sniff the IP Packets and Print Destination MAC Address
def sniff_IP_MAC(pkt):
    print("Source MAC: %s <-----> Dest MAC: %s" %(pkt[Ether].src,pkt[Ether].dst))

#Sniffing TCP data of Port 80 and displaying SRC and DST IP alson with HTTP Payload
def sniff_IP_PAYLOAD(pkt):
    print("Source IP: {} <--HTTP--> Dest IP: {} Dest Port: {}  Payload:\n{}\n\n".format(pkt[IP].src,pkt[IP].dst,pkt[TCP].dport,pkt[TCP].payload))

#Callback Function to sniff ARP packets and Print Request and Response IP and MAC addresses
def sniff_ARP(pkt):
    if pkt[ARP].op == 1: #who-has (request)
        return 'Request: {} is asking about {}'.format(pkt[ARP].psrc, pkt[ARP].pdst)
    if pkt[ARP].op == 2: #is-at (response)
        return '*Response: {} has address {}'.format(pkt[ARP].hwsrc, pkt[ARP].psrc)


print("Choose From the Below options:")
print("----------------------------------------- \n")
print("\t 1) Sniff TCP packets and display src and dest IP packets \n\t 2) Sniff the IP Packets and print src and dest. IP addresses\n\t 3) Sniff the IP Packets and Print Destination MAC Address\n\t 4) Sniff ARP Packets and Print Request and Response IP and MAC addresses")

while(1):
	choice = int(input())

	if choice == 1:
        	sniff(filter='tcp',prn=sniff_TCP, count=10)

	elif choice == 2:
        	sniff(filter='ip', prn=sniff_IP, count=10)

	elif choice == 3:
    	         sniff(filter='ip', prn=sniff_IP_MAC, count=10)

	elif choice == 4:
        	sniff(filter='arp', prn=sniff_ARP, count=10)

	elif choice == 5:
        	sniff(filter='ip', prn=sniff_IP_PAYLOAD, count=10)

	else:
    	        pass



#sniff(filter='IP',prn=sniffing, count=10)

