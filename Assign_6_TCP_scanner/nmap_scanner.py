#importing necessary libraries
import nmap
from optparse import OptionParser

#Usage Info 
Usage='Usage: python3 <program> --hosts <hosts range> [ 194.456.234.56/24; 194.456.234.56-256 ] --ports <port range> [ 1-100 ]'

#Insatntiating parser object
parser = OptionParser(Usage)

#adding --hosts argument to store hosts range to be scanned
parser.add_argument('--hosts', action="store", dest="hosts")

#Adding --ports argument to provie Port / Port Range
parser.add_argument('--ports', action="store", dest="ports")

(options,args) = parser.parse_args()

#storing host and port range
ip_range = options.hosts
port_range = options.ports

#Instantiating an object for Scanning Port
nm = nmap.PortScanner()

#Scanning Port as provided in arguments
nm.scan(ip_range,port_range)

#Iterating all hosts with up status
for host in nm.all_hosts():
	state = nm[host].state()
	print("Scanned: %s \t State: %s" %(host,state))
	#Iterating protocols on a host
	for protocols in nm[host].all_protocols():
		ports_list = nm[host][protocols].keys()
		#Iterating port in a protocol on a host
		for port in ports_list:
			#Storing the State of the Port (Open/Close)
			#nm['11.11.3.205']['tcp'][22]['state']
			pstate = nm[host][protocols][port]['state']
			#Storing name of the Port Service (http,ssh..)
			#nm['11.11.3.205']['tcp'][80]['name']
			pname = nm[host][protocols][port]['name']
			print("Port:%s \t State:%s \t Service:%s" %(port,pstate,pname))
		#print port
	print("")
	


