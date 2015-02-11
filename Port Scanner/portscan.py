from socket import *
from threading import *

screenLock = Semaphore(value = 1)

def connScan(tgtHost, tgtPort):
	try:
		connSkt = socket(AF_INET, SOCK_STREAM)
		connSkt.connect((tgtHost, tgtPort))
		connSkt.send("hello\r\n")

		results = connSkt.recv(100)
		screenLock.acquire()
		print str(tgtPort) + "/tcp open"
	except:
		screenLock.acquire()
		print str(tgtPort)+ "/tcp closed"
	finally:
		screenLock.release()
		connSkt.close()

def portScan(tgtHost, tgtPorts):
	try:
		tgtIP = gethostbyname(tgtHost)
	except:
		print "Cannot resolve " +tgtHost+ ": Unknown host"
		return

	try:
		tgtName = gethostbyaddr(tgtIP)
		print "\nScan Results for" + tgtName[0]
	except:
		print "\n Scan results for" + tgtIP
	setdefaulttimeout(1)
	for tgtPort in tgtPorts:
		#t = Thread(target = connScan, args = (tgtHost, int(tgtPort)))
		#t.start()
		connScan(tgtHost,tgtPort)

def Main():
	f_port = 0
	l_port = 0
	tgtHost = raw_input("Enter hostname/IP address: ")
	while True:
		#f_port = int(raw_input("Enter first port to check (1 - 65535)"))
		if (f_port<=0) or (f_port>65535):
			f_port = int(raw_input("Enter first port to check (1 - 65535)"))
		else:
			break

	while True:
		#l_port = int(raw_input("Enter last port to check (0- 65535)"))
		if (l_port<=0) or (l_port>65535) or (l_port<f_port):
			l_port = int(raw_input("Enter last port to check (0 - 65535)"))
		else:
			break

	tgtPorts = range(f_port,l_port+1)
	portScan(tgtHost,tgtPorts)




if __name__ == "__main__":
	Main()